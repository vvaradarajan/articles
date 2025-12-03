!application: borrowNotBuy
# form Generator application (generates form  from yaml file)!
# Section components to be imported in client
!componentJs: ./borrowNotBuy/cComponents.js
!def_detail: borrow
# section that goes into the html page (using the components defined in the previous line)
<menu-element>
<form-gen serverUrlPrefix="${serverUrlPrefix}/borrowNotBuy" ${attribs}></form-gen>
</menu-element>
