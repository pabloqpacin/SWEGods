var gods = [{
      id: 1,
      name: "Zeus",
      power: "Sky, weather, kings, fate",
      parents: "Kronos and Rhea",
      olympian: "yes",
      children: "Aphrodite, Phersephone, Hercules",
      symbol: "Lightning bolt, eagle, bull",
      counterpart: "Jupiter"
  },{
    id: 2,
    name: "Poseidon",
    power: "King of the Sea, earthquakes, floods, horses",
    parents: "Kronos and Rhea",
    olympian: "yes",
    children: "Triton, Nerids",
    symbol: "Trident, Bull, horse, dolphin",
    counterpart: "Neptune"
  },{
    id: 3,
    name: "Hades",
    power: "God of the dead, king of the underworld",
    parents: "Kronos and Rhea",
    olympian: "yes",
    children: "Cerberus, the Erinyes",
    symbol: "Royal sceptre, cornucopia",
    counterpart: "Pluto"
  }];


  ReactDOM.render(
    <div style={{marginTop: 50 + 'px'}}>
      <BootstrapTable data={gods} striped={true} hover={true} pagination={true}>
          <TableHeaderColumn dataField="id" isKey={true} dataAlign="center" dataSort={true}>Product ID</TableHeaderColumn>
          <TableHeaderColumn dataField="name" dataSort={true}>Name</TableHeaderColumn>
          <TableHeaderColumn dataField="power" dataSort={true}>Power</TableHeaderColumn>
          <TableHeaderColumn dataField="parents" dataSort={true}>Parents</TableHeaderColumn>
          <TableHeaderColumn dataField="olympian" dataSort={true}>Olympian</TableHeaderColumn>
          <TableHeaderColumn dataField="children" dataSort={true}>Children</TableHeaderColumn>
          <TableHeaderColumn dataField="symbol" dataSort={true}>Symbol</TableHeaderColumn>
          <TableHeaderColumn dataField="counterpart" dataSort={true}>Counterpart</TableHeaderColumn>
      </BootstrapTable>
    </div>,
      document.getElementById("gods")
  );
