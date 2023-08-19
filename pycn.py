def pycn_run(func):
    import io,sys,re
    
    module={
        "数学":"math",
        "时间":"time",
        "操作系统":"os",
        "正则表达式":"re",
        "命令行":"sys",
        "随机":"random"
    }
    
    keyword={
        # 内置函数
        r"绝对值（.*?）":(lambda x:f"abs({x.group()[4:-1]})"),
        r"全部（.*?）":(lambda x:f"all({x.group()[3:-1]})"),
        r"任意（.*?）":(lambda x:f"any({x.group()[3:-1]})"),
        r"代码（.*?）":(lambda x:f"ascii({x.group()[3:-1]})"),
        r"二进制（.*?）":(lambda x:f"bin({x.group()[4:-1]})"),
        r"布尔值（.*?）":(lambda x:f"bool({x.group()[4:-1]})"),
        r"输出（.*?）":(lambda x:f"print({x.group()[3:-1]})"),
        r"字节数组（.*?）":(lambda x:f"bytearray({x.group()[5:-1]})"),
        r"可调用（.*?）":(lambda x:f"callable({x.group()[4:-1]})"),
        r"字符（.*?）":(lambda x:f"chr({x.group()[3:-1]})"),
        r"类方法（.*?）":(lambda x:f"classmethod({x.group()[4:-1]})"),
        r"编译（.*?）":(lambda x:f"compile({x.group()[3:-1]})"),
        r"复数（.*?）":(lambda x:f"complex({x.group()[3:-1]})"),
        r"删除属性（.*?）":(lambda x:f"delattr({x.group()[5:-1]})"),
        r"字典（.*?）":(lambda x:f"dict({x.group()[3:-1]})"),
        r"目录（.*?）":(lambda x:f"dir({x.group()[3:-1]})"),
        r"带余除法（.*?）":(lambda x:f"divmod({x.group()[5:-1]})"),
        r"枚举（.*?）":(lambda x:f"enumerate({x.group()[3:-1]})"),
        r"解析（.*?）":(lambda x:f"eval({x.group()[3:-1]})"),
        r"执行（.*?）":(lambda x:f"exec({x.group()[3:-1]})"),
        r"过滤（.*?）":(lambda x:f"filter({x.group()[3:-1]})"),
        r"浮点数（.*?）":(lambda x:f"float({x.group()[4:-1]})"),
        r"获取属性（.*?）":(lambda x:f"getattr({x.group()[5:-1]})"),
        r"全局变量（.*?）":(lambda x:f"globals({x.group()[5:-1]})"),
        r"包含属性（.*?）":(lambda x:f"hasattr({x.group()[5:-1]})"),
        r"哈希值（.*?）":(lambda x:f"hash({x.group()[4:-1]})"),
        r"帮助（.*?）":(lambda x:f"help({x.group()[3:-1]})"),
        r"十六进制（.*?）":(lambda x:f"hex({x.group()[5:-1]})"),
        r"地址（.*?）":(lambda x:f"id({x.group()[3:-1]})"),
        r"输入（.*?）":(lambda x:f"input({x.group()[3:-1]})"),
        r"整数（.*?）":(lambda x:f"int({x.group()[3:-1]})"),
        r"是否为类（.*?）":(lambda x:f"isinstance({x.group()[5:-1]})"),
        r"是否子类（.*?）":(lambda x:f"issubclass({x.group()[5:-1]})"),
        r"迭代（.*?）":(lambda x:f"iter({x.group()[3:-1]})"),
        r"长度（.*?）":(lambda x:f"len({x.group()[3:-1]})"),
        r"列表（.*?）":(lambda x:f"list({x.group()[3:-1]})"),
        r"局部变量（.*?）":(lambda x:f"locals({x.group()[5:-1]})"),
        r"映射（.*?）":(lambda x:f"map({x.group()[3:-1]})"),
        r"最大值（.*?）":(lambda x:f"max({x.group()[4:-1]})"),
        r"存储（.*?）":(lambda x:f"memoryview({x.group()[3:-1]})"),
        r"最小值（.*?）":(lambda x:f"min({x.group()[4:-1]})"),
        r"下一个（.*?）":(lambda x:f"next({x.group()[4:-1]})"),
        r"对象（.*?）":(lambda x:f"object({x.group()[3:-1]})"),
        r"八进制（.*?）":(lambda x:f"oct({x.group()[4:-1]})"),
        r"打开（.*?）":(lambda x:f"open({x.group()[3:-1]})"),
        r"顺序（.*?）":(lambda x:f"ord({x.group()[3:-1]})"),
        r"幂（.*?）":(lambda x:f"pow({x.group()[2:-1]})"),
        r"输出（.*?）":(lambda x:f"print({x.group()[3:-1]})"),
        r"属性（.*?）":(lambda x:f"property({x.group()[3:-1]})"),
        r"范围（.*?）":(lambda x:f"range({x.group()[3:-1]})"),
        r"代言（.*?）":(lambda x:f"repr({x.group()[3:-1]})"),
        r"输出（.*?）":(lambda x:f"print({x.group()[3:-1]})"),
        r"反转（.*?）":(lambda x:f"reversed({x.group()[3:-1]})"),
        r"四舍五入（.*?）":(lambda x:f"round({x.group()[5:-1]})"),
        r"集合（.*?）":(lambda x:f"set({x.group()[3:-1]})"),
        r"设置属性（.*?）":(lambda x:f"setattr({x.group()[5:-1]})"),
        r"切片（.*?）":(lambda x:f"slice({x.group()[3:-1]})"),
        r"排序（.*?）":(lambda x:f"sorted({x.group()[3:-1]})"),
        r"静态方法（.*?）":(lambda x:f"staticmethod({x.group()[5:-1]})"),
        r"字符串（.*?）":(lambda x:f"str({x.group()[4:-1]})"),
        r"求和（.*?）":(lambda x:f"sum({x.group()[3:-1]})"),
        r"调用父类（.*?）":(lambda x:f"super({x.group()[5:-1]})"),
        r"元组（.*?）":(lambda x:f"tuple({x.group()[3:-1]})"),
        r"类型（.*?）":(lambda x:f"type({x.group()[3:-1]})"),
        r"变量（.*?）":(lambda x:f"vars({x.group()[3:-1]})"),
        r"打包（.*?）":(lambda x:f"zip({x.group()[3:-1]})"),
        r"导库（.*?）":(lambda x:f"__import__({x.group()[3:-1]})"),
        
        # 关键字
        r"导入 .*?":(lambda x:f"import {x.group()[3:]}"),
        r"从 .*?":(lambda x:f"from {x.group()[2:]}"),
        r"作为 .*?":(lambda x:f"as {x.group()[3:]}"),
        r"否则如果 .*?":(lambda x:f"elif {x.group()[5:]}"),
        r"如果 .*?":(lambda x:f"if {x.group()[3:]}"),
        r"否则":(lambda x:"else"),
        r"匹配 .*?":(lambda x:f"match {x.group()[3:]}"),
        r"箱子 .*?":(lambda x:f"import {x.group()[3:]}"),
        r"当 .*?":(lambda x:f"while {x.group()[2:]}"),
        r"给 .*?":(lambda x:f"for {x.group()[2:]}"),
        r"不在 .*?":(lambda x:f"not in {x.group()[3:]}"),
        r"在 .*?":(lambda x:f"in {x.group()[2:]}"),
        r"不是 .*?":(lambda x:f"is not {x.group()[3:]}"),
        r"是 .*?":(lambda x:f"is {x.group()[2:]}"),
        r"类 .*?":(lambda x:f"class {x.group()[2:]}"),
        r"尝试":(lambda x:"try"),
        r"除外 .*?":(lambda x:f"except {x.group()[3:]}"),
        r"最后 .*?":(lambda x:f"finally {x.group()[3:]}"),
        r"用 .*?":(lambda x:f"with {x.group()[2:]}"),
        r"举起 .*?":(lambda x:f"raise {x.group()[3:]}"),
        r"断言 .*?":(lambda x:f"assert {x.group()[3:]}"),
        r"定义 .*?":(lambda x:f"def {x.group()[3:]}"),
        r"匿名函数 .*?":(lambda x:f"lambda {x.group()[5:]}"),
        r"全局 .*?":(lambda x:f"global {x.group()[3:]}"),
        r"返回 .*?":(lambda x:f"return {x.group()[3:]}"),
        r"产生 .*?":(lambda x:f"yield {x.group()[3:]}"),
        r"删除 .*?":(lambda x:f"del {x.group()[3:]}"),
        r" 与 .*?":(lambda x:f" and {x.group()[3:]}"),
        r" 或 .*?":(lambda x:f" or {x.group()[3:]}"),
        r"否 .*?":(lambda x:f"not {x.group()[2:]}"),
        r"停止":(lambda x:"break"),
        r"继续":(lambda x:"continue"),
        r"通过":(lambda x:"pass"),
        r"真":(lambda x:"True"),
        r"假":(lambda x:"False"),
        r"空":(lambda x:"None"),
        r"自己":(lambda x:"self"),
        r"原类":(lambda x:"cls"),
        
        # 异常
        "语法异常":(lambda x:"SyntaxError"),
        "变量异常":(lambda x:"ValueError"),
        "索引异常":(lambda x:"IndexError"),
        "键值异常":(lambda x:"KeyError"),
        "缩进异常":(lambda x:"TabError"),
        "名字异常":(lambda x:"NameError"),
        "类型异常":(lambda x:"TypeError"),
        "除数为0异常":(lambda x:"ZeroDivisionError"),
        "导入异常":(lambda x:"ValueError"),
        "变量异常":(lambda x:"ValueError"),
        "编码异常":(lambda x:"UnicodeError"),
        "属性异常":(lambda x:"AttributeError"),
        "文件查找异常":(lambda x:"FileNotFoundError"),
        "异常":(lambda x:f"Exception"),
        
        # 随机库函数
        r"种子（.*?）":(lambda x:f"seed({x.group()[3:-1]})"),
        r"随机数（.*?）":(lambda x:f"random({x.group()[4:-1]})"),
        r"随机取整（.*?）":(lambda x:f"randint({x.group()[5:-1]})"),
        r"随机小数（.*?）":(lambda x:f"uniform({x.group()[5:-1]})"),
        r"随机范值（.*?）":(lambda x:f"randrange({x.group()[5:-1]})"),
        r"随机字节（.*?）":(lambda x:f"randbytes({x.group()[5:-1]})"),
        r"选择（.*?）":(lambda x:f"choice({x.group()[3:-1]})"),
        r"打乱顺序（.*?）":(lambda x:f"shuffle({x.group()[5:-1]})"),
        
        # 数学库函数
        r"向上取整（.*?）":(lambda x:f"ceil({x.group()[5:-1]})"),
        r"向下取整（.*?）":(lambda x:f"floor({x.group()[5:-1]})"),
        r"以e为底对数（.*?）":(lambda x:f"log({x.group()[7:-1]})"),
        r"以2为底对数（.*?）":(lambda x:f"log2({x.group()[7:-1]})"),
        r"以10为底对数（.*?）":(lambda x:f"log10({x.group()[8:-1]})"),
        r"平方根（.*?）":(lambda x:f"sqrt({x.group()[4:-1]})"),
        r"e的次幂（.*?）":(lambda x:f"exp({x.group()[5:-1]})"),
        r"最大公因数（.*?）":(lambda x:f"gcd({x.group()[6:-1]})"),
        r"最大公约数（.*?）":(lambda x:f"gcd({x.group()[6:-1]})"),
        r"向上取整（.*?）":(lambda x:f"ceil({x.group()[5:-1]})"),
        r"正弦（.*?）":(lambda x:f"sin({x.group()[3:-1]})"),
        r"余弦（.*?）":(lambda x:f"cos({x.group()[3:-1]})"),
        r"正切（.*?）":(lambda x:f"tan({x.group()[3:-1]})"),
        r"反正弦（.*?）":(lambda x:f"asin({x.group()[4:-1]})"),
        r"反余弦（.*?）":(lambda x:f"acos({x.group()[4:-1]})"),
        r"反正切（.*?）":(lambda x:f"atan({x.group()[4:-1]})"),
        r"双曲正弦（.*?）":(lambda x:f"sinh({x.group()[5:-1]})"),
        r"双曲余弦（.*?）":(lambda x:f"cosh({x.group()[5:-1]})"),
        r"双曲正切（.*?）":(lambda x:f"tanh({x.group()[5:-1]})"),
        r"反双曲正弦（.*?）":(lambda x:f"asinh({x.group()[6:-1]})"),
        r"反双曲余弦（.*?）":(lambda x:f"acosh({x.group()[6:-1]})"),
        r"反双曲正切（.*?）":(lambda x:f"atanh({x.group()[6:-1]})"),
        r"派":(lambda x:"pi"),
        r"自然对数":(lambda x:"e"),
        r"无穷大":(lambda x:"inf"),
        r"非数字":(lambda x:"nan"),
        
        # 时间库函数
        r"时间戳（.*?）":(lambda x:f"time({x.group()[4:-1]})"),
        r"睡眠（.*?）":(lambda x:f"sleep({x.group()[3:-1]})"),
        r"解格式化时间（.*?）":(lambda x:f"strptime({x.group()[7:-1]})"),
        r"格式化时间（.*?）":(lambda x:f"strftime({x.group()[6:-1]})"),
        r"世界时间（.*?）":(lambda x:f"gmtime({x.group()[7:-1]})"),
        r"当地时间（.*?）":(lambda x:f"localtime({x.group()[5:-1]})"),
        
        # 操作系统库函数
        r"运行系统（.*?）":(lambda x:f"system({x.group()[5:-1]})"),
        r"当前路径（.*?）":(lambda x:f"getcwd({x.group()[5:-1]})"),
        r"获取用户名（.*?）":(lambda x:f"getuid({x.group()[6:-1]})"),
        r"终端尺寸（.*?）":(lambda x:f"get_terminal_size({x.group()[5:-1]})"),
        r"目名文件（.*?）":(lambda x:f"listdir({x.group()[5:-1]})"),
        r"创建目名（.*?）":(lambda x:f"mkdir({x.group()[5:-1]})"),
        r"删除目名（.*?）":(lambda x:f"rmdir({x.group()[5:-1]})"),
        r"重命名（.*?）":(lambda x:f"rename({x.group()[4:-1]})"),
        r"删除（.*?）":(lambda x:f"remove({x.group()[3:-1]})"),
        
        # 命令行库函数
        r"参数":(lambda x:"argv"),
        r"模块":(lambda x:"modules"),
        r"平台":(lambda x:"platform"),
        r"版本":(lambda x:"version"),
        r"编码格式（.*?）":(lambda x:f"getdefaultencoding({x.group()[5:-1]})"),
        r"输入流":(lambda x:"stdin"),
        r"输出流":(lambda x:"stdout"),
        r"。输入（.*?）":(lambda x:f".read({x.group()[4:-1]})"),
        r"。输出（.*?）":(lambda x:f".write({x.group()[4:-1]})"),
        r"。输出不换行（.*?）":(lambda x:f".writelines({x.group()[7:-1]})"),
        r"退出（.*?）":(lambda x:f"exit({x.group()[3:-1]})"),
        
        # 正则表达式
        r"匹配（.*?）":(lambda x:f"match({x.group()[3:-1]})"),
        r"替换（.*?）":(lambda x:f"sub({x.group()[3:-1]})"),
        r"查找（.*?）":(lambda x:f"findall({x.group()[3:-1]})"),
        r"分开（.*?）":(lambda x:f"split({x.group()[3:-1]})"),
        r"搜索（.*?）":(lambda x:f"search({x.group()[3:-1]})"),
    }
    
    symbol={
        "（":"(",
        "）":")",
        "【":"[",
        "】":"]",
        "｛":"{",
        "｝":"}",
        "‘":"\'",
        "’":"\'",
        "“":"\"",
        "”":"\"",
        "，":",",
        "。":".",
        "：":":",
        "；":";",
        "—":"_",
        "、":"\\"
    }
    
    out=io.StringIO()
    sys.stdout=out
    help(func)
    sys.stdout=sys.__stdout__
    code=out.getvalue()
    code=code.split("\n")[3:-1]
    code=[c[4:len(c)] for c in code]
    code="\n".join(code)
    
    for k in keyword:
        while re.findall(k,code):
            code=re.sub(k,keyword[k],code)
    
    for s in symbol:
        code=code.replace(s,symbol[s])
        
    for m in module:
        code=code.replace(m,module[m])
        
    for s in symbol:
        code=code.replace("\\"+symbol[s],s)
        
    for m in module:
        code=code.replace("\\"+module[m],m)
    
    exec(code)
