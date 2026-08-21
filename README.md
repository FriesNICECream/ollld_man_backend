# ollld_man_backend

用于学习 Python、FastAPI、SQLAlchemy、Alembic 和 PostgreSQL 的后端项目。

当前阶段只建立可运行的技术骨架，不包含领域模型、CRUD、认证或其他业务逻辑。业务代码由仓库维护者在学习过程中自行完成。

## 环境要求

- Python 3.12
- Poetry 2.x
- Docker 与 Docker Compose

## 首次启动

```bash
git clone https://github.com/FriesNICECream/ollld_man_backend.git
cd ollld_man_backend

cp .env.example .env
poetry install
docker compose up -d postgres
poetry run alembic upgrade head
poetry run uvicorn app.main:app --reload
```

访问：

- 健康检查：<http://127.0.0.1:8000/health>
- Swagger UI：<http://127.0.0.1:8000/docs>

健康检查预期返回：

```json
{"status": "ok"}
```

## 最小验证清单

```bash
docker compose ps
poetry run python -c "from app.main import app; print(app.title)"
poetry run alembic current
poetry run ruff check .
curl http://127.0.0.1:8000/health
```

验证标准：

- PostgreSQL 容器状态为 healthy
- FastAPI 应用可以被 Python 导入
- Alembic 可以连接数据库且命令无报错
- Ruff 检查通过
- `/health` 返回 HTTP 200 和 `{"status":"ok"}`

## 目录边界

```text
app/
├── core/       # 环境与应用配置
├── db/         # SQLAlchemy 连接和声明式基类
└── main.py     # FastAPI 启动入口与系统健康检查
migrations/     # Alembic 迁移环境；暂时没有业务迁移
```

暂不添加：

- 业务实体和数据库表
- Repository、Service 或 Use Case
- CRUD API
- 用户、认证和权限
- 为展示架构而创建的空业务分层

当你开始第一个业务练习时，再按实际用例逐步增加结构。
