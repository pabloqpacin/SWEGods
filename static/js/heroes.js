var heroes = [{
      id: 1,
      name: "Hercules",
      parents: "Zeus and Alcmene",
      type: "Demigod",
      power: "Bow and arrow, champion wrestler, superhuman strength, intelligence",
      death: "N/A",
      origin: "The Twelve Labors"
  },{
    id: 2,
    name: "Odysseus",
    parents: "N/A",
    type: "Human",
    power: "Versatility, brilliance",
    death: "Killed by Telegonus",
    origin: "The Odyssey: ten eventful years he took to return home after the Trojan War"
  },{
    id: 3,
    name: "Perseus",
    parents: "Zeus and Danae",
    type: "Demigod",
    power: "N/A",
    death: "Died of old age",
    origin: "Killed Medusa"
  }];

  function onRowSelect(row, isSelected){
    window.location.href = '/heroes/' + row.name.toLowerCase().replace(/ /gi,'');
  }

  var selectRowProp = {
    mode: "radio",
    clickToSelect: true,
    bgColor: "rgb(238, 193, 213)",
    onSelect: onRowSelect
  };

  ReactDOM.render(
    <div style={{marginTop: 50 + 'px'}}>
      <BootstrapTable data={heroes} striped={true} hover={true} pagination={true} selectRow={selectRowProp}>
          <TableHeaderColumn dataField="id" isKey={true} dataAlign="center" dataSort={true}>Product ID</TableHeaderColumn>
          <TableHeaderColumn dataField="name" dataSort={true}>Name</TableHeaderColumn>
          <TableHeaderColumn dataField="parents" dataSort={true}>Birth Parents</TableHeaderColumn>
          <TableHeaderColumn dataField="type" dataSort={true}>Type</TableHeaderColumn>
          <TableHeaderColumn dataField="power" dataSort={true}>Strength or Power</TableHeaderColumn>
          <TableHeaderColumn dataField="death" dataSort={true}>Death</TableHeaderColumn>
          <TableHeaderColumn dataField="origin" dataSort={true}>Hero Orgins</TableHeaderColumn>
      </BootstrapTable>
    </div>,
      document.getElementById("heroes")
  );
