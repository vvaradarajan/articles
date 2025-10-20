!application: htmlPage
# Chess application (Has puzzles and championship game)
# Section components to be imported in client
!componentJs: ./htmlPage/cComponents.js
# section that goes into the html page (using the components defined in the previous line)
<menu-element>
<html-out serverUrlPrefix="${serverUrlPrefix}/htmlPage" fileNm="yogaLogic.html"></html-out>
</menu-element>