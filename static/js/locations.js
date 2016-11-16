console.log(LocationsList);

var Table = Reactable.Table,
    unsafe = Reactable.unsafe;

var bgColors = { "Default": "#81b71a",
                    "Blue": "#00B1E1",
                    "Cyan": "#37BC9B",
                    "Green": "#8CC152",
                    "Red": "#E9573F",
                    "Yellow": "#F6BB42",
};

var locationsinfo = [];
for (var i = 0; i < LocationsList.length; i++) {
    var location = {
      'Name': unsafe('<a href="/locations/' + LocationsList[i].name.toLowerCase() + '">' + LocationsList[i].name + '</a>'),
      'Alternate Name': unsafe(LocationsList[i].altname),
      'Type': unsafe(LocationsList[i].location_type),
      'Myth': unsafe(LocationsList[i].myth),
      'Characters': unsafe(LocationsList[i].gods)
    };
    locationsinfo.push(location);
}

ReactDOM.render(
  <div>
    <Table className="table" id="table" style={{backgroundColor: bgColors.Yellow}}

    data={locationsinfo}

    sortable={[
      {
          column: 'Name',
          sortFunction: function(a, b){
              // Sort by last name
              var nameA = a
              var nameB = b

              return nameA.localeCompare(nameB);
          }
      },
      'Alternate Name',
      'Type',
      'Myth',
      'Characters'
    ]}

    filterable={['Name', 'Alternate Name', 'Type', 'Myth', 'Characters']}

    defaultSort={{column: 'Name', direction: 'asc'}} itemsPerPage={8} pageButtonLimit={100}/>
  </div>,
    document.getElementById('locations')
);
