admin.py  是Django的一个用于管理任务的命令行工具
app.py  用于定义该应用程序的一些基本信息和配置项
models.py：Django 模型的定义，用于 ORM 数据库交互。
serializers.py：使用 Django REST Framework 定义的序列化器，用于将模型数据转换为 JSON 格式的数据。
views.py：使用 Django REST Framework 定义的视图函数，用于处理 API 请求和响应。
urls.py：应用程序的 URL 配置文件，定义 API 的路由。
migrations文件夹用于存储数据库迁移相关的文件和信息。数据库迁移是一种管理数据库架构变化的方法，可以轻松地在开发过程中添加、修改或删除。
__pycache__ 文件夹是 Python 解释器在执行模块导入时自动生成的一个特殊文件夹。它用于存储编译后的字节码文件，以便提高后续导入相同模块时的执行速度。