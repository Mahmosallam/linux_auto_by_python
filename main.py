import mod1
import mod2
import mod3
import mod4
from mod3 import change_owner


mod1.configure_system("intranet.xyz.local")
mod2.users_adding_process()
mod3.set_permissions()
mod4.main()
change_owner("/var/www/html","developer1")
change_owner("/var/www/html/index.html","developer1")