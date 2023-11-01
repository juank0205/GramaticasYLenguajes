"""
Script to generate an AST from a logical expression using plyplus.
"""

import sys
from plyplus import Grammar
from ASTTraverser import ASTTraverser

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"Example call: {sys.argv[0]} expr.txt output.png")
    else:
        sourceFile = sys.argv[1]
        ASTFile = sys.argv[2]
        with open('bool.g', 'r', encoding='utf-8') as grm:
            with open(sourceFile, 'r', encoding='utf-8') as sc:
                scode = sc.read()
                # Create the AST for the expression written in sourceFile
                ast = Grammar(grm.read(), auto_filter_tokens=False).parse(scode)
                # Export AST as an image 
                ast.to_png_with_pydot(ASTFile)
                # Visit and evaluate
                t = ASTTraverser()
                t.visit(ast)
                print(t.getTranslation())
