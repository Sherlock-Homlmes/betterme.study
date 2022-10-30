import requests

from pydantic import BaseModel, EmailStr

from all_env import bot_api


class DiscordUser(BaseModel):
    id: int
    email: EmailStr
    name: str 
    avatar_url: str
    gender: str | None
    age_range: str | None

    def register(self):
        pass
        # joined_at= datetime(*map(int, self.joined_at))

    def login(self):
        pass

    def update(self) -> bool:

        resp = requests.get(url=f"{bot_api}member/{self.id}")
        if resp.status_code != 200:
            return False

        sv_user_info = resp.json()
        print(sv_user_info)
        self.gender=sv_user_info['gender']
        self.age_range=sv_user_info['age_range']

        return True