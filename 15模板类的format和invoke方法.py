from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import FewShotPromptTemplate
from langchain_core.prompts import ChatPromptTemplate


template = PromptTemplate.from_template("我的邻居是:{lastname}，最喜欢：{hobby}")
res = template.format(lastname="张大妈",hobby="钓鱼")
print(res,type(res))

res2=template.invoke({"lastname":"张大妈","hobby":"钓鱼"})
print(res2,type(res2))