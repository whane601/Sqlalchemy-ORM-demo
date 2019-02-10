from src.common import util

from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(util.get_config_value("DB", "MYSQL"))
Base = automap_base()

class GlobalWine(Base):

    __tablename__ = "global_wine"
    __mapper_args__ = {
        "exclude_properties" : ["foodpairing", "winery", "region"]
    }

Base.prepare(engine, reflect=True)
Session = sessionmaker(bind=engine)
session = Session()

CwWine = Base.classes.cw_wine
GlobalVintageWine = Base.classes.global_vintage_wine

if __name__ == "__main__":

    query_resault = session.query(
        CwWine.member_id,
        GlobalWine.display_name,
        GlobalVintageWine.vintage
    ).join(
        GlobalVintageWine, CwWine.global_vintage_wine_id == GlobalVintageWine.id
    ).join(
        GlobalWine, GlobalVintageWine.global_wine_id == GlobalWine.id
    ).filter(
        CwWine.member_id == 3
    )

    for item in query_resault:
        print(item)