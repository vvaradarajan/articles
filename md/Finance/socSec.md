!application: socSec
# form Generator application (generates form  from yaml file)!
# Section components to be imported in client
!componentJs: ./socSec/cComponents.js
# section that defines variables to substitute into the html
!def_detail: socSec
# section that goes into the initial html page (using the components defined in the previous line)
<menu-element>
<ss-form serverUrlPrefix="${serverUrlPrefix}/socSec" ${attribs}></ss-form>
</menu-element>
