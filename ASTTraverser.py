class ASTTraverser(object):
    def __init__(self):
        self.translation = ""

    def getTranslation(self):
        return self.translation

    ##############################
    ## Methods to visit the AST ##
    ##############################
    def visit(self, tree):
        # print("Visitor")
        method = getattr(self, tree.head, None)
        # print("Visit for {} will call {}".format(tree.head, method))
        if method:
            return method(tree)
        else:
            print(f"Method {method} is not defined by the class")

    def start(self, tree):
        # print(f"Start*- {tree}")
        self.visit(tree.tail[0])

    def logicalexpression(self, tree):
        # print(f"Logical Expression: {tree}"
        self.visit(tree.tail[0])
    
    def parexpr(self, tree):
        self.translation += str(tree.tail[0])
        self.visit(tree.tail[1])
        self.translation += str(tree.tail[2])

    def neg(self, tree):
        self.translation += str(tree.tail[0])
        self.visit(tree.tail[1])
    
    def binexpr(self, tree):
        self.visit(tree.tail[0])
        self.visit(tree.tail[1])
        self.visit(tree.tail[2])

    def andexpr(self, tree):
        self.translation += " & "
        print(tree.tail[0])

    def orexpr(self, tree):
        self.translation += " | "

    def impexpr(self, tree):
        self.translation += "!"
        self.visit(tree.tail[0])
        self.translation += " | "
        self.visit(tree.tail[2])

    def dimpexpr(self, tree):
        self.translation += "((!"
        self.visit(tree.tail[0])
        self.translation += " | "
        self.visit(tree.tail[2])
        self.translation += ") & (!"
        self.visit(tree.tail[0])
        self.translation += " | "
        self.visit(tree.tail[2])
        self.translation += "))"

    def ifexpr(self, tree):
        self.visit(tree.tail[1])
        self.translation += " & "
        self.visit(tree.tail[3])

    def ifelseexpr(self, tree):
        self.translation += "("
        self.visit(tree.tail[1])
        self.translation += " & "
        self.visit(tree.tail[3])
        self.translation += ") | (!"
        self.visit(tree.tail[1])
        self.translation += " & "
        self.visit(tree.tail[5])
        self.translation += ")"

# CONDITIONAL EXPRESSIONS

    def variable(self, tree):
        self.translation += str(tree.tail[0])
