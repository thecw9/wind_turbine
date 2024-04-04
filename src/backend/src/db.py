from datetime import datetime

import aiohttp
from sqlalchemy import create_engine, insert, select, update
from sqlalchemy.orm import Session
from src.authentication import generate_token
from src.config import Config
from src.logger import Logger
from src.orm_model import AuthUser, Devices, Measures
from src.orm_model.base import Base
from src.services.nrmock_service import get_all_measures_info_from_nrmock_service

config = Config()
logger = Logger(__name__)

engine = create_engine(config.DATABASE_URI, echo=False)


async def init_db():
    if config.DEBUG:
        logger.info("drop all tables")
        # Base.metadata.drop_all(engine)

    Base.metadata.create_all(engine)
    logger.info("init auth user table")
    init_auth_user_table()
    logger.info("init measures table")
    await init_measures_table()
    logger.info("init fusion model table")
    await init_devices_table()
    logger.info("reflect db")
    reflect_db()


def reflect_db():
    # all tables start with "measures_" prefix
    Base.metadata.reflect(bind=engine)


def init_auth_user_table():
    # AuthUser
    with Session(engine) as session:
        # check user is exist
        statement = select(AuthUser).where(AuthUser.username == config.FIRST_SUPERUSER)
        user = session.execute(statement).scalar_one_or_none()

        if not user:
            # Create a default user
            user = AuthUser(
                username=config.FIRST_SUPERUSER,
                email=config.FIRST_SUPERUSER_EMAIL,
                password=config.FIRST_SUPERUSER_PASSWORD,
                access_token=generate_token(config.FIRST_SUPERUSER, config.SECRETE_KEY),
                is_active=True,
                is_superuser=True,
                created_at=datetime.now(),
                updated_at=datetime.now(),
            )
            session.add(user)
            session.commit()


async def init_measures_table():
    # check measures data is exist
    with Session(engine) as session:
        statement = select(Measures).limit(1)
        result = session.execute(statement).scalars().all()
        if result:
            logger.info("measures data is exist")
            return

    # Measures
    async with aiohttp.ClientSession() as aiohttp_session:
        measures_info = await get_all_measures_info_from_nrmock_service(
            session=aiohttp_session
        )

    measures = [
        {
            "key": i.get("scadaid"),
            "time": i.get("time_stamp"),
            "value": i.get("fvalue"),
            "unit": i.get("unitsymbol"),
            "name": i.get("name"),
            "path": i.get("path"),
            "quality": i.get("quality"),
        }
        for i in measures_info
    ]

    with Session(engine) as session:
        # insert measures
        session.execute(
            insert(Measures),
            measures,
        )
        session.commit()


async def init_devices_table():
    # check fusion model data is exist
    with Session(engine) as session:
        statement = select(Devices).limit(1)
        result = session.execute(statement).scalars().all()
        if result:
            logger.info("fusion model data is exist")
            return

    # FusionModel

    fusion_models = [
        # #1号机组 ~ #13号机组
        {
            "key": 5000000000000000,
            "path": "/融合/画笔山风电场/#1号机组/",
            "include": "画笔山风电场AND#1号机组AND发电机"
            + " OR 画笔山风电场AND#1号机组AND齿轮箱"
            + " OR 画笔山风电场AND#1号机组AND主轴承"
            + " OR 画笔山风电场AND#1号机组AND变频器"
            + " OR 画笔山风电场AND#1号机组AND偏航"
            + " OR 画笔山风电场AND#1号机组AND默认变量",
            "exclude": "红外",
        },
        {
            "key": 5000000000000001,
            "path": "/融合/画笔山风电场/#2号机组/",
            "include": "画笔山风电场AND#2号机组AND发电机"
            + " OR 画笔山风电场AND#2号机组AND齿轮箱"
            + " OR 画笔山风电场AND#2号机组AND主轴承"
            + " OR 画笔山风电场AND#2号机组AND变频器"
            + " OR 画笔山风电场AND#2号机组AND偏航"
            + " OR 画笔山风电场AND#2号机组AND默认变量",
            "exclude": "红外",
        },
        {
            "key": 5000000000000002,
            "path": "/融合/画笔山风电场/#3号机组/",
            "include": "画笔山风电场AND#3号机组AND发电机"
            + " OR 画笔山风电场AND#3号机组AND齿轮箱"
            + " OR 画笔山风电场AND#3号机组AND主轴承"
            + " OR 画笔山风电场AND#3号机组AND变频器"
            + " OR 画笔山风电场AND#3号机组AND偏航"
            + " OR 画笔山风电场AND#3号机组AND默认变量",
            "exclude": "红外",
        },
        {
            "key": 5000000000000003,
            "path": "/融合/画笔山风电场/#4号机组/",
            "include": "画笔山风电场AND#4号机组AND发电机"
            + " OR 画笔山风电场AND#4号机组AND齿轮箱"
            + " OR 画笔山风电场AND#4号机组AND主轴承"
            + " OR 画笔山风电场AND#4号机组AND变频器"
            + " OR 画笔山风电场AND#4号机组AND偏航"
            + " OR 画笔山风电场AND#4号机组AND默认变量",
            "exclude": "红外",
        },
        {
            "key": 5000000000000004,
            "path": "/融合/画笔山风电场/#5号机组/",
            "include": "画笔山风电场AND#5号机组AND发电机"
            + " OR 画笔山风电场AND#5号机组AND齿轮箱"
            + " OR 画笔山风电场AND#5号机组AND主轴承"
            + " OR 画笔山风电场AND#5号机组AND变频器"
            + " OR 画笔山风电场AND#5号机组AND偏航"
            + " OR 画笔山风电场AND#5号机组AND默认变量",
            "exclude": "红外",
        },
        {
            "key": 5000000000000005,
            "path": "/融合/画笔山风电场/#6号机组/",
            "include": "画笔山风电场AND#6号机组AND发电机"
            + " OR 画笔山风电场AND#6号机组AND齿轮箱"
            + " OR 画笔山风电场AND#6号机组AND主轴承"
            + " OR 画笔山风电场AND#6号机组AND变频器"
            + " OR 画笔山风电场AND#6号机组AND偏航"
            + " OR 画笔山风电场AND#6号机组AND默认变量",
            "exclude": "红外",
        },
        {
            "key": 5000000000000006,
            "path": "/融合/画笔山风电场/#7号机组/",
            "include": "画笔山风电场AND#7号机组AND发电机"
            + " OR 画笔山风电场AND#7号机组AND齿轮箱"
            + " OR 画笔山风电场AND#7号机组AND主轴承"
            + " OR 画笔山风电场AND#7号机组AND变频器"
            + " OR 画笔山风电场AND#7号机组AND偏航"
            + " OR 画笔山风电场AND#7号机组AND默认变量",
            "exclude": "红外",
        },
        {
            "key": 5000000000000007,
            "path": "/融合/画笔山风电场/#8号机组/",
            "include": "画笔山风电场AND#8号机组AND发电机"
            + " OR 画笔山风电场AND#8号机组AND齿轮箱"
            + " OR 画笔山风电场AND#8号机组AND主轴承"
            + " OR 画笔山风电场AND#8号机组AND变频器"
            + " OR 画笔山风电场AND#8号机组AND偏航"
            + " OR 画笔山风电场AND#8号机组AND默认变量",
            "exclude": "红外",
        },
        {
            "key": 5000000000000008,
            "path": "/融合/画笔山风电场/#9号机组/",
            "include": "画笔山风电场AND#9号机组AND发电机"
            + " OR 画笔山风电场AND#9号机组AND齿轮箱"
            + " OR 画笔山风电场AND#9号机组AND主轴承"
            + " OR 画笔山风电场AND#9号机组AND变频器"
            + " OR 画笔山风电场AND#9号机组AND偏航"
            + " OR 画笔山风电场AND#9号机组AND默认变量",
            "exclude": "红外",
        },
        {
            "key": 5000000000000009,
            "path": "/融合/画笔山风电场/#10号机组/",
            "include": "画笔山风电场AND#10号机组AND发电机"
            + " OR 画笔山风电场AND#10号机组AND齿轮箱"
            + " OR 画笔山风电场AND#10号机组AND主轴承"
            + " OR 画笔山风电场AND#10号机组AND变频器"
            + " OR 画笔山风电场AND#10号机组AND偏航"
            + " OR 画笔山风电场AND#10号机组AND默认变量",
            "exclude": "红外",
        },
        {
            "key": 5000000000000010,
            "path": "/融合/画笔山风电场/#11号机组/",
            "include": "画笔山风电场AND#11号机组AND发电机"
            + " OR 画笔山风电场AND#11号机组AND齿轮箱"
            + " OR 画笔山风电场AND#11号机组AND主轴承"
            + " OR 画笔山风电场AND#11号机组AND变频器"
            + " OR 画笔山风电场AND#11号机组AND偏航"
            + " OR 画笔山风电场AND#11号机组AND默认变量",
            "exclude": "红外",
        },
        {
            "key": 5000000000000011,
            "path": "/融合/画笔山风电场/#12号机组/",
            "include": "画笔山风电场AND#12号机组AND发电机"
            + " OR 画笔山风电场AND#12号机组AND齿轮箱"
            + " OR 画笔山风电场AND#12号机组AND主轴承"
            + " OR 画笔山风电场AND#12号机组AND变频器"
            + " OR 画笔山风电场AND#12号机组AND偏航"
            + " OR 画笔山风电场AND#12号机组AND默认变量",
            "exclude": "红外",
        },
        {
            "key": 5000000000000012,
            "path": "/融合/画笔山风电场/#13号机组/",
            "include": "画笔山风电场AND#13号机组AND发电机"
            + " OR 画笔山风电场AND#13号机组AND齿轮箱"
            + " OR 画笔山风电场AND#13号机组AND主轴承"
            + " OR 画笔山风电场AND#13号机组AND变频器"
            + " OR 画笔山风电场AND#13号机组AND偏航"
            + " OR 画笔山风电场AND#13号机组AND默认变量",
            "exclude": "红外",
        },
    ]

    with Session(engine) as session:
        # insert measures
        session.execute(
            insert(Devices),
            fusion_models,
        )
        session.commit()
