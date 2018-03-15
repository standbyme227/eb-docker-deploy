# EC2 Deploy project

AWS의 EC2 배포를 연습하는 프로젝트입니다.
`.secrets`폴더내의 파일로 비밀 키를 관리합니다.

DB로 PostgreSQL을 사용하며, `local`환경에서는 `localhost`의 DB, `dev`환경과 `production`환경에서는 `AWS RDS`의 DB를 사용합니다.



## 환경 구분

### local

외부 서비스 접근 없이 개발 환경만을 사용 (DB와 Storage를 전부 로컬환경에서 구성)



### dev

DB, Storage에 외부 서비스 (AWS RDS, S3)를 사용



### production

실제 배포 환경






## Requirements

### 로켈 테스트

- Python (3.6)


### AWS 환경 테스트

- Python (3.6)
- S3 Bucket, 해당 Bucket을 사용할 수있는 IAM User의 AWS ACCESS KEY, SECRET ACCESS KET
- RDS Database(보안그룹 허용 필요), 해당 Database를 사용할 수 있는 RDS의 user name, password




## Installation

```
pip install -r .requirements/dev.txt
python manage.py runserver
```





## Secrets

**`.secrets/base.json`**

```json
{
  "SECRET_KEY": "<Django settings SECRET_KEY value>"
}

{
  "SECRET_KEY":"<Django settings SECRET_KEY value>",
  "RAVEN_CONFIG":{
    "dsn": "<RAVEN SECRET TOKEN>",
    "release": "raven.fetch_git_sha(os.path.abspath(os.pardir))"
  },
  "SUPERUSER_USERNAME": "<SUPERUSER's username>",
  "SUPERUSER_PASSWORD": "<SUPERUSER's password>",
  "SUPERUSER_EMAIL": "<SUPERUSER's email>"

  "AWS_ACCESS_KEY_ID": "AWS의 액세스키 .aws/credentials 참조",
  "AWS_SECRET_ACCESS_KEY": "AWS 비밀 액세스 키 .aws/credentials 참조",
  "AWS_STORAGE_BUCKET_NAME": "S3의 버킷 네임",

  "AWS_DEFAULT_ACL" : "private",
  "AWS_S3_REGION_NAME" : "지역",
  "AWS_S3_SIGNATURE_VERSION" : "s3v4"
}
```

**`.secrets/dev.json & production.json`**

```json
{
  "DATABASES": {
    "default": {
      "ENGINE": "django.db.backends.postgresql",
      "HOST": "rds 앤드포인트",
      "NAME": "DB Name",
      "USER": "DB의 사용자",
      "PASSWORD": "비밀번호",
      "PORT": 5432
    }
  }
}
```





