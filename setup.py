from setuptools import find_packages,setup

setup(
    name = 'mcqgenerator',
    version = '0.0.1',
    author = 'virendra chaudhary',
    author_email = 'virendremoond@gmail.com',
    install_recquires = ["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages = find_packages()
)