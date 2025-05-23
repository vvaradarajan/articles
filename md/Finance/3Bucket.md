!application: retirement
# form Generator application (generates form  from yaml file)!
# Section components to be imported in client
!componentJs: ./retirement/cComponents.js
!def_detail: retirement
# section that goes into the html page (using the components defined in the previous line)
<menu-element>
<form-gen serverUrlPrefix="${serverUrlPrefix}/retirement" ${attribs}></form-gen>
</menu-element>
