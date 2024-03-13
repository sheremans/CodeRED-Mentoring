/Users/anastasiasheremet/Desktop/python/test_morse_code_translator_2_py.py:1
=============================== FAILURES ===============================
______________________________ test_main _______________________________

    def test_main():
>       user_input = input("provide the proof: ")

test_morse_code_translator_2_py.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_pytest.capture.DontReadFromInput object at 0x105f42210>
size = -1

    def read(self, size: int = -1) -> str:
>       raise OSError(
            "pytest: reading from stdin while output is captured!  Consider using `-s`."
        )
E       OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.

/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/_pytest/capture.py:207: OSError
------------------------- Captured stdout call -------------------------
provide the proof: 
======================= short test summary info ========================
FAILED test_morse_code_translator_2_py.py::test_main - OSError: pytest: reading from stdin while output is captured!  Cons...
ERROR test_morse_code_translator_2_py.py::test_text_to_morse
====================== 1 failed, 1 error in 0.05s ======================
anastasiasheremet@Anastasias-MacBook-Pro python % pytest
========================= test session starts ==========================
platform darwin -- Python 3.12.0, pytest-8.1.1, pluggy-1.4.0
rootdir: /Users/anastasiasheremet/Desktop/python
plugins: anyio-4.0.0
collected 2 items / 1 error                                            

================================ ERRORS ================================
____________ ERROR collecting test_Morse_code_translator.py ____________
test_Morse_code_translator.py:19: in <module>
    user_input = input("provide the proof: ")
/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/_pytest/capture.py:207: in read
    raise OSError(
E   OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.
--------------------------- Captured stdout ----------------------------
provide the proof: 
======================= short test summary info ========================
ERROR test_Morse_code_translator.py - OSError: pytest: reading from stdin while output is captured!  Cons...
!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!
=========================== 1 error in 0.07s ===========================
anastasiasheremet@Anastasias-MacBook-Pro python % 