!application: chess
# Chess application (Has puzzles and championship game)
# Section components to be imported in client
!componentJs: ./chess/cComponents.js
!def_detail: mateIn2Easy
# section that goes into the html page (using the components defined in the previous line)
<menu-element>
<chess-game serverUrlPrefix="${serverUrlPrefix}/chess" ${attribs}></chess-game>
</menu-element>
