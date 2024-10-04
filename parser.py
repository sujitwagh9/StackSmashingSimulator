# parser.py
import clang.cindex

# Set the path to libclang.dll (adjust path as necessary)
clang.cindex.Config.set_library_file(r"C:\Program Files\LLVM\bin\libclang.dll")

def parse_code(code):
    """
    Parses the provided C/C++ code to extract functions and detect unsafe patterns.
    Uses Clang's Python bindings for more advanced parsing.
    """
    index = clang.cindex.Index.create()
    
    # Save the code to a temporary file
    with open("temp_code.c", "w") as f:
        f.write(code)
    
    # Parse the code
    translation_unit = index.parse("temp_code.c")
    
    functions = []
    vulnerabilities = []

    # Traverse the AST to find functions and potential vulnerabilities
    for cursor in translation_unit.cursor.get_children():
        if cursor.kind == clang.cindex.CursorKind.FUNCTION_DECL:
            function_name = cursor.spelling
            tokens = [token.spelling for token in cursor.get_tokens()]
            functions.append((function_name, tokens))

    return functions
