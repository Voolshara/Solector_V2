import sqlalchemy as sa
from sqlalchemy import  func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import and_

import os
from dotenv import load_dotenv
from contextlib import contextmanager


dotenv_path = os.path.join(os.path.dirname(__file__) + '/../', '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

engine = sa.create_engine(
    'postgresql://{}:{}@{}:{}/{}'.format(
        os.getenv('PARSER_PG_NAME'),
        os.getenv('PARSER_PG_PASSWORD'),
        os.getenv('PARSER_PG_HOST'),
        os.getenv('PARSER_PG_PORT'),
        os.getenv('PARSER_PG_DB_NAME'),
    )
)
Session = sessionmaker(bind=engine)
Base = declarative_base()

@contextmanager
def create_session(**kwargs):
    new_session = Session(**kwargs)
    try:
        yield new_session
        new_session.commit()
    except Exception:
        new_session.rollback()
        raise
    finally:
        new_session.close()


class Panel_Producers(Base):
    __tablename__ = "producers_producers"
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String())


class Panels(Base):
    __tablename__ = 'panels'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String())
    link_name = sa.Column(sa.String())
    cost = sa.Column(sa.Integer)
    power = sa.Column(sa.Integer)
    efficiency = sa.Column(sa.Float)
    img_link = sa.Column(sa.String())
    producer = sa.Column(sa.Integer, sa.ForeignKey(Panel_Producers.id))
    panel_link = sa.Column(sa.String())


class DB_get:
    def __init__(self):
        pass

    def get_marketplace_data(self):
        with create_session() as session:
            db_response = session.query(Panel_Producers).all()
            all_producers = [i.name for i in db_response]
            db_response = session.query(
                func.max(Panels.power).label("max_power"), 
                func.min(Panels.power).label("min_power"),
                func.max(Panels.cost).label("max_cost"), 
                func.min(Panels.cost).label("min_cost"),
                ).one()
            return {
                'brands' : all_producers,
                'power' : [db_response.min_power, db_response.max_power],
                'cost' : [db_response.min_cost, db_response.max_cost]
                }

    def get_panels(self, filters):
        with create_session() as session:
            if filters['brands'] is None:
                db_response = session.query(Panel_Producers).all()
                brands_ids = [i.id for i in db_response]
            else:    
                brands_ids = []
                for brand in filters['brands'].keys():
                    if filters['brands'][brand]:
                        db_response = session.query(Panel_Producers).filter(
                            Panel_Producers.name == brand).one_or_none()
                        if db_response is not None:
                            brands_ids.append(db_response.id)
            
            if filters['power'] is None:
                db_response = session.query(
                func.max(Panels.power).label("max_power"), 
                func.min(Panels.power).label("min_power"),).one()
                min_power = db_response.min_power
                max_power = db_response.max_power
            else:
                min_power = filters['power'][0]
                max_power = filters['power'][1]

            if filters['cost'] is None:
                db_response = session.query(
                func.max(Panels.cost).label("max_cost"), 
                func.min(Panels.cost).label("min_cost"),).one()
                min_cost = db_response.min_cost
                max_cost = db_response.max_cost
            else:
                min_cost = filters['cost'][0]
                max_cost = filters['cost'][1]

            db_response = session.query(Panels).filter(and_(
                Panels.producer.in_(brands_ids), 
                Panels.power >= min_power, Panels.power <= max_power,
                Panels.cost >= min_cost, Panels.cost <= max_cost
            )).all()

            PANELS = []
            for el in db_response:
                db_response = session.query(Panel_Producers).filter(
                        Panel_Producers.id == el.producer).one_or_none()
                producer = db_response.name
                PANELS.append({
                    'name' : el.name,
                    'link_name' : el.link_name,
                    'cost' : el.cost,
                    'power' : el.power,
                    'efficiency' : el.efficiency,
                    'img' : el.img_link,
                    'producer' : producer,
                    'panel_link' : el.panel_link,
                })
            return PANELS

    def get_product(self, product):
        with create_session() as session:
            db_response = session.query(Panels).filter(Panels.link_name == product).one_or_none()
            producer_response = session.query(Panel_Producers).filter(Panel_Producers.id == db_response.producer).one_or_none()
            return {
                    'name' : db_response.name,
                    'cost' : db_response.cost,
                    'power' : db_response.power,
                    'efficiency' : db_response.efficiency,
                    'img' : db_response.img_link,
                    'producer' : producer_response.name,
                    'panel_link' : db_response.panel_link,
                }


class DB_new:
    def __init__(self) -> None:
        self.PRODUCERS = ["Hevel Solar", "Телеком СТВ"]

    def create_all_tables(self):
        Base.metadata.create_all(engine)
        self.set_all_producers()
        self.set_all_panels()
    
    def set_all_producers(self):
        for el in self.PRODUCERS:
            with create_session() as session:
                status_response = session.query(Panel_Producers).filter(Panel_Producers.name == el).one_or_none()
                if status_response is None:
                    session.add(Panel_Producers(name=el))
    
    def set_all_panels(self):
        PANELS = [
            ['HVL-390/HJT', 18290, 390, 19.5, 'https://www.hevelsolar.com/loaded/catalog/goods/thumbs/1e0f6c8ea7310cb04c09bd64585b1dbf.png', self.PRODUCERS.index("Hevel Solar") + 1, 'https://www.hevelsolar.com/catalog/solnechnye-moduli/modul-fotoelektricheskii-hvl-390hjt/'],
            ['HVL-385/HJT', 17990, 385, 19.3, 'https://www.hevelsolar.com/loaded/catalog/goods/thumbs/5b53904ed9cd5f236149a8ac690a391b.png', self.PRODUCERS.index("Hevel Solar") + 1, 'https://www.hevelsolar.com/catalog/solnechnye-moduli/modul-fotoelektricheskii-hvl-385hjt/'],
            ['HVL-380/HJT', 17790, 380, 19.0, 'https://www.hevelsolar.com/loaded/catalog/goods/thumbs/a67b37db6ad01447c822b8456735ea23.png', self.PRODUCERS.index("Hevel Solar") + 1, 'https://www.hevelsolar.com/catalog/solnechnye-moduli/modul-fotoelektricheskii-hvl-380hjt/'],
            ['HVL-375/HJT', 17590, 375, 18.75, 'https://www.hevelsolar.com/loaded/catalog/goods/thumbs/604097ab1566a473899ffc99ecca3bea.png', self.PRODUCERS.index("Hevel Solar") + 1, 'https://www.hevelsolar.com/catalog/solnechnye-moduli/modul-fotoelektricheskii-hvl-375hjt/'],
            ['HVL-370/HJT', 17390, 370, 18.5, 'https://www.hevelsolar.com/loaded/catalog/goods/thumbs/9b6aad14499577f19ac2d0fc1e193618.png', self.PRODUCERS.index("Hevel Solar") + 1, 'https://www.hevelsolar.com/catalog/solnechnye-moduli/modul-fotoelektricheskii-hvl-370hjt/'],
            ['HVL-365/HJT', 17090, 365, 18.25, 'https://www.hevelsolar.com/loaded/catalog/goods/thumbs/215b0bed55c475d34426d9dc424ded6c.png', self.PRODUCERS.index("Hevel Solar") + 1, 'https://www.hevelsolar.com/catalog/solnechnye-moduli/modul-fotoelektricheskii-hvl-365hjt/'],
            ['HVL-360/HJT', 16890, 360, 18.0, 'https://www.hevelsolar.com/loaded/catalog/goods/c0a68703e15a31c6023882eb93da4c24.png', self.PRODUCERS.index("Hevel Solar") + 1, 'https://www.hevelsolar.com/catalog/solnechnye-moduli/modul-fotoelektricheskii-hvl-360hjt/'], 
            ['HVL-330/HJT', 15190, 330, 19.7, 'https://www.hevelsolar.com/loaded/catalog/goods/thumbs/952a2d8b9b474c4b944017296059fa8c.png', self.PRODUCERS.index("Hevel Solar") + 1, 'https://www.hevelsolar.com/catalog/solnechnye-moduli/modul-fotoelektricheskii-hvl-330hjt/'],
            ['HVL-325/HJT', 14890, 325, 19.4, 'https://www.hevelsolar.com/loaded/catalog/goods/thumbs/6c68e7070956697c50acbef7ce409fc3.png', self.PRODUCERS.index("Hevel Solar") + 1, 'https://www.hevelsolar.com/catalog/solnechnye-moduli/modul-fotoelektricheskii-hvl-325hjt/'],
            ['HVL-320/HJT', 14690, 320, 19.1, 'https://www.hevelsolar.com/loaded/catalog/goods/thumbs/c0d67c470705d50255e7fe2a18aebdf5.png', self.PRODUCERS.index("Hevel Solar") + 1, 'https://www.hevelsolar.com/catalog/solnechnye-moduli/modul-fotoelektricheskii-hvl-320hjt/'],
            ['HVL-315/HJT', 14490, 315, 19.04, 'https://www.hevelsolar.com/loaded/catalog/goods/thumbs/5aaeb9180bf2bf03883f1ddd2fb8a8e2.png', self.PRODUCERS.index("Hevel Solar") + 1, 'https://www.hevelsolar.com/catalog/solnechnye-moduli/modul-fotoelektricheskii-hvl-315hjt/'],
            ['HVL-310/HJT', 14290, 310, 18.76, 'https://www.hevelsolar.com/loaded/catalog/goods/thumbs/d8abfc5093c85171a3f493eaaab4ce62.png', self.PRODUCERS.index("Hevel Solar") + 1, 'https://www.hevelsolar.com/catalog/solnechnye-moduli/modul-fotoelektricheskii-hvl-310hjt/'],
            ['HVL-300/HJT', 12190, 300, 17.98, 'https://www.hevelsolar.com/loaded/catalog/goods/thumbs/32524347c166bbd0dc9d3d0752014186.png', self.PRODUCERS.index("Hevel Solar") + 1, 'https://www.hevelsolar.com/catalog/solnechnye-moduli/modul-fotoelektricheskii-hvl-300hjt/'],
            ['HVL-290/HJT', 11790, 290, 17.32, 'https://www.hevelsolar.com/loaded/catalog/goods/thumbs/2b0e51dd36d1f49671cc6c5755f5bed8.png', self.PRODUCERS.index("Hevel Solar") + 1, 'https://www.hevelsolar.com/catalog/solnechnye-moduli/modul-fotoelektricheskii-hvl-290hjt/'],
            ['HVL-270/HJT', 10990, 270, 16.12, 'https://www.hevelsolar.com/loaded/catalog/goods/thumbs/085770ce2086d0c1b5c7675d52b181a9.png', self.PRODUCERS.index("Hevel Solar") + 1, 'https://www.hevelsolar.com/catalog/solnechnye-moduli/modul-fotoelektricheskii-hvl-270hjt/'],
            ['HVL-260/HJT', 10590, 260, 15.53, 'https://www.hevelsolar.com/loaded/catalog/goods/thumbs/84def46e327046071a6e8ff3d7357d45.png', self.PRODUCERS.index("Hevel Solar") + 1, 'https://www.hevelsolar.com/catalog/solnechnye-moduli/modul-fotoelektricheskii-hvl-260hjt/'],
            ['HVL-250/HJT', 10190, 250, 14.93, 'https://www.hevelsolar.com/loaded/catalog/goods/thumbs/bda26942eda46c5e2020d255ec1f64c8.png', self.PRODUCERS.index("Hevel Solar") + 1, 'https://www.hevelsolar.com/catalog/solnechnye-moduli/modul-fotoelektricheskii-hvl-250hjt/'],
            ['HVL-125/O', 4625, 125, 8.74, 'https://www.hevelsolar.com/loaded/catalog/goods/thumbs/39a6d1c0e23a39d94e1634d81fbcb95e.png', self.PRODUCERS.index("Hevel Solar") + 1, 'https://www.hevelsolar.com/catalog/solnechnye-moduli/modul-fotoelektricheskii-hvl-125o/'],
            ['HVL-120/O', 4440, 120, 8.39, 'https://www.hevelsolar.com/loaded/catalog/goods/thumbs/2b50dda52fb68e3f53073a9c3244a69d.png', self.PRODUCERS.index("Hevel Solar") + 1, 'https://www.hevelsolar.com/catalog/solnechnye-moduli/modul-fotoelektricheskii-hvl-120o/'],
            ['HVL-115/O', 4255, 115, 7.9, 'https://www.hevelsolar.com/loaded/catalog/goods/thumbs/217d0489dbc4b3030d54fbc0f228988f.png', self.PRODUCERS.index("Hevel Solar") + 1, 'https://www.hevelsolar.com/catalog/solnechnye-moduli/modul-fotoelektricheskii-hvl-115o/'],
            ['HVL-105/O', 3885, 105, 7.34, 'https://www.hevelsolar.com/loaded/catalog/goods/thumbs/6e1e3514129ed0baba18d3cd89606927.png', self.PRODUCERS.index("Hevel Solar") + 1, 'https://www.hevelsolar.com/catalog/solnechnye-moduli/modul-fotoelektricheskii-hvl-105o/'],

            ['ТСМ-15', 4126, 18, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-50', 7500, 54, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-80А', 11916, 85, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-80B', 12168, 85, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-90А', 12600, 90, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-90B', 12852, 90, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-110А', 15529, 115, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-110В', 15771, 115, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-145А', 20160, 150, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-145В', 20412, 150, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-170А', 20640, 175, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-170В', 20892, 175, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-180А', 21240, 180, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-180В', 21468, 180, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-240А', 24538, 240, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-240В', 24780, 240, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-270А', 28440, 270, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-280А', 27994, 280, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-290А', 30240, 290, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-300А', 31320, 300, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-30', 5610, 30, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-50', 7400, 49, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-65', 8850, 65, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-70', 9360, 70, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-75', 9600, 75, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-100А', 14184, 100, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-100B', 14508, 100, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-120А', 16920, 125, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-120В', 17130, 125, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-130А', 17400, 134, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-130В', 17640, 134, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-150А', 17856, 155, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-150В', 18098, 155, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-200А', 22119, 200, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-200В', 22361, 200, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-250А', 25575, 250, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-250B', 25817, 250, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-30S', 8136, 33, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-115S', 19469, 120, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-160S', 25229, 165, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-230SА', 34884, 230, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules'],
            ['ТСМ-230SВ', 34884, 230, None, 'http://www.telstv.ru/imgs/solarModules.jpg', self.PRODUCERS.index("Телеком СТВ") + 1, 'http://www.telstv.ru/?page=ru_solar_modules']
        ]

        
        for name, cost, power, eff, img, producer, panel_link in PANELS:
            with create_session() as session:
                status_response = session.query(Panels).filter(Panels.name == name).one_or_none()
                if status_response is None:
                    session.add(Panels(name=name,
                                    link_name = "-".join(name.split('/')),
                                    cost=cost,
                                    power=power,
                                    efficiency=eff,
                                    img_link=img,
                                    producer=producer,
                                    panel_link=panel_link))


# DBN = DB_new()
# DBN.create_all_tables()

# fil = {'brands': {'Hevel Solar': True}, 'power': [200, 390], 'cost': [15000, 34000]}
# DBG = DB_get()
# DBG.get_panels(fil)