import asyncio
import asyncpg
from data import config


class Database():
    def __init__(self):
        loop = asyncio.get_event_loop()
        self.pool: asyncio.pool.Pool = loop.run_until_complete(
            asyncpg.create_pool(
                user=config.PGUSER,
                database=config.DBNAME,
                password=config.PGPASSWORD,
                host=config.HOST,
                port=config.DBPORT
            )
        )

    async def get_wheel_info(self, id):
        sql = f"""
        SELECT category_careers, category_environment,
        category_family, category_hobbies, category_rest,
        category_education, category_health_sport FROM public.users
        WHERE id = '{id}'
        """

        await self.pool.execute(sql)

    async def insert_table_user(self, id, name, phone):
        sql = f"""
        INSERT INTO public."users"(
        id, name, phone)
        VALUES ({id}, '{name}', '{phone}');
        """

        await self.pool.execute(sql)

    async def update_careers_category(self, id, amount):
        sql = f"""
        UPDATE public."users"
        SET category_careers = category_careers + {amount}
        WHERE users.id = '{id}'
        """

        await self.pool.execute(sql)

    async def update_family_category(self, id, amount):
        sql = f"""
        UPDATE public."users"
        SET category_family = category_family + {amount}
        WHERE users.id = '{id}'
        """

        await self.pool.execute(sql)

    async def update_environment_category(self, id, amount):
        sql = f"""
        UPDATE public."users"
        SET category_environment = category_environment + {amount}
        WHERE users.id = '{id}'
        """

        await self.pool.execute(sql)

    async def update_hobbies_category(self, id, amount):
        sql = f"""
        UPDATE public."users"
        SET category_hobbies = category_hobbies + {amount}
        WHERE users.id = '{id}'
        """

        await self.pool.execute(sql)
    
    async def update_rest_category(self, id, amount):
        sql = f"""
        UPDATE public."users"
        SET category_rest = category_rest + {amount}
        WHERE users.id = '{id}'
        """

        await self.pool.execute(sql)

    async def update_education_category(self, id, amount):
        sql = f"""
        UPDATE public."users"
        SET category_education = category_education + {amount}
        WHERE users.id = '{id}'
        """

        await self.pool.execute(sql)

    async def update_health_category(self, id, amount):
        sql = f"""
        UPDATE public."users"
        SET category_health_sport = category_health_sport + {amount}
        WHERE users.id = '{id}'
        """

        await self.pool.execute(sql)

    async def drop_wheel(self, id):
        sql = f"""
        UPDATE public.users
        SET category_careers=0, category_environment=0, category_family=0,
        category_hobbies=0, category_rest=0, category_education=0, category_health_sport=0
        WHERE id = '{id}'
        """
        await self.pool.execute(sql)

    async def edit_careers_category(self, id, amount):
        sql = f"""
        UPDATE public."users"
        SET category_careers = {amount}
        WHERE users.id = '{id}'
        """

        await self.pool.execute(sql)

    async def edit_family_category(self, id, amount):
        sql = f"""
        UPDATE public."users"
        SET category_family = {amount}
        WHERE users.id = '{id}'
        """

        await self.pool.execute(sql)

    async def edit_environment_category(self, id, amount):
        sql = f"""
        UPDATE public."users"
        SET category_environment = {amount}
        WHERE users.id = '{id}'
        """

        await self.pool.execute(sql)

    async def edit_hobbies_category(self, id, amount):
        sql = f"""
        UPDATE public."users"
        SET category_hobbies = {amount}
        WHERE users.id = '{id}'
        """

        await self.pool.execute(sql)

    async def edit_rest_category(self, id, amount):
        sql = f"""
        UPDATE public."users"
        SET category_rest = {amount}
        WHERE users.id = '{id}'
        """

        await self.pool.execute(sql)

    async def edit_education_category(self, id, amount):
        sql = f"""
        UPDATE public."users"
        SET category_education = {amount}
        WHERE users.id = '{id}'
        """

        await self.pool.execute(sql)

    async def edit_health_category(self, id, amount):
        sql = f"""
        UPDATE public."users"
        SET category_health_sport = {amount}
        WHERE users.id = '{id}'
        """

        await self.pool.execute(sql)

    async def edit_wheel(self, id):
        sql = f"""
        UPDATE public.users
        SET category_careers=0, category_environment=0, category_family=0,
        category_hobbies=0, category_rest=0, category_education=0, category_health_sport=0
        WHERE id = '{id}'
        """
        await self.pool.execute(sql)

    async def select_categories(self, id):
        sql = f"""
        SELECT *
        FROM public.users
        WHERE id = '{id}'
        """
        ans = []
        try:
            rows = await self.pool.fetch(sql)
            for row in rows:
                return row
        except:
            pass
