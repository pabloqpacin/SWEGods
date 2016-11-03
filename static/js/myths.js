var myths = [{
      id: 1,
      myth: "Flight of Daedalus and Icarus",
      main_characters: "Icarus, Daedalus, Minotaur",
      related_gods: "N/A",
      summary: "Flight of Daedalys and Icarus",
      location: "Crete",
      impact: "A man who does not recognise his own limitations"
  },{
    id: 2,
    myth: "Myth of Perseus",
    main_characters: "Perseus, Polydectes",
    related_gods: "Hermes, Athenea",
    summary: "Myth of Perseus",
    location: "Argos",
    impact: "Nature of fate and prophecies"
  },{
    id: 3,
    myth: "Orpheus and Eurydice",
    main_characters: "Orpheus",
    related_gods: "Dionysus, Hades",
    summary: "Myth of Orpheus and Eurydice",
    location: "N/A",
    impact: "Romantic love is a dangerous thing"
  }];

  function onRowSelect(row, isSelected){
    window.location.href = '/myths/' + row.myth.toLowerCase().replace(/ /gi,'');;
  }

  var selectRowProp = {
    mode: "radio",
    clickToSelect: true,
    bgColor: "rgb(238, 193, 213)",
    onSelect: onRowSelect
  };

  ReactDOM.render(
    <div style={{marginTop: 50 + 'px'}}>
      <BootstrapTable data={myths} striped={true} hover={true} pagination={true} selectRow={selectRowProp}>
          <TableHeaderColumn dataField="id" isKey={true} dataAlign="center" dataSort={true}>Product ID</TableHeaderColumn>
          <TableHeaderColumn dataField="myth" dataSort={true}>Myth</TableHeaderColumn>
          <TableHeaderColumn dataField="main_characters" dataSort={true}>Main Charactres</TableHeaderColumn>
          <TableHeaderColumn dataField="related_gods" dataSort={true}>Related Gods</TableHeaderColumn>
          <TableHeaderColumn dataField="summary" dataSort={true}>Summary</TableHeaderColumn>
          <TableHeaderColumn dataField="location" dataSort={true}>Location</TableHeaderColumn>
          <TableHeaderColumn dataField="impact" dataSort={true}>Impact on Greek Life</TableHeaderColumn>
      </BootstrapTable>
    </div>,
      document.getElementById("myths")
  );
