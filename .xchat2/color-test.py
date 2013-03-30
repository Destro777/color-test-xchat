import xchat
__module_name__ = "color test text"
__module_version__ = "1.0.0"
__module_description__ = "seeing how to print out colors to xchat"

#Color : 0x03 = 003 = %C (with 2 digits after, f.e. \00304 = color 4) 

colorTest1 = "say \002\037\00309hi this is Neon Green"
colorTest2 = "say \00304hi this is red"
colorTest3 = "say \x0304this is also red"

xchat.command(colorTest1)
xchat.command(colorTest2)
xchat.command(colorTest3)

#Format Type   Octal Escape Code   HexaD Escape Code   Control Escape Code
#Bold               \002	         \x02	               \cB
#Color	            \003	         \x03	               \cC
#Underline	        \037	         \x1F	               \c_
#Original Color	    \017	         \x0F	               \cO
#Reverse Color	    \026	         \x16	               \cV
#Beep	            \007	         \x07	               \cG
