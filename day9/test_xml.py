# Author:xqkang
# Date:2020/10/12 下午2:10
import xml.etree.ElementTree as ET

# tree = ET.parse("xml_test.xml")
tree = ET.parse("test.xml")
root = tree.getroot()
# print(root)
# print(root.tag)

# for child in root:
#     print(child.tag, child.text, child.attrib)
#     for i in child:
#         print(i.tag, i.text, i.attrib)

# # 取自结束标签
# for node in root:
#     print(node.attrib)

# 获得某个字段
for node in root.iter("year"):
    print(node.tag, node.text)

# 修改
# for node in root.iter("year"):
#     node_year = int(node.text) + 1
#     node.text = str(node_year)
#     node.set("update", "yes")
# tree.write("test.xml")

# 删除
for country in root.findall("country"):
    rank = int(country.find("rank").text)
    if rank > 50:
        root.remove(country)

tree.write("output.xml")

