from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_env: str = "local"
    database_url: str = "postgresql+psycopg://incident:incident@localhost:5432/incident"
    # 모델 호출 단계에서 사용한다. 절대 코드에 직접 넣지 말고 .env로만 주입한다.
    anthropic_api_key: str = ""


settings = Settings()
