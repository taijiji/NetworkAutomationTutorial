import jinja2

# ファイルの読み込み
file = open("sample_template.jinja2", "r")
template_txt = file.read()
print(template_txt)

# １つのテンプレート(雛形)から１つのテキストファイルを作成する例
# テンプレートオブジェクトの作成
template = jinja2.Environment().from_string(template_txt)

# テンプレートに値を代入
config_txt = template.render(
    if_description="To_RouterA",
    if_name="fastethernet 1/1",
    ip4='192.168.0.1',
    ip4_subnet="255.255.255.0")

print(config_txt)

# １つのテンプレート(雛形)から複数のテキストファイルを作成する例
interfaces = [
    {
        "if_description" : "To_RouterA",
        "if_name" : "fastethernet 1/1",
        "ip4" : "192.168.0.1",
        "ip4_subnet" : "255.255.255.0"
    },
    {
        "if_description" : "To_RouterB",
        "if_name" : "fastethernet 1/2",
        "ip4" : "192.168.1.1",
        "ip4_subnet" : "255.255.255.0"
    },
    {
        "if_description" : "To_RouterC",
        "if_name" : "fastethernet 1/3",
        "ip4" : "192.168.2.1",
        "ip4_subnet" : "255.255.255.0"
    }
]

for interface in interfaces:
    config_txt = template.render(interface)
    print(config_txt)
