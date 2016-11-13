console.log(GodsList);

var Table = Reactable.Table,
    unsafe = Reactable.unsafe;

var bgColors = { "Default": "#81b71a",
                    "Blue": "#00B1E1",
                    "Cyan": "#37BC9B",
                    "Green": "#8CC152",
                    "Red": "#E9573F",
                    "Yellow": "#F6BB42",
};

var godsinfo = [];
for (var i = 0; i < GodsList.length; i++) {
    var god = {
      'Name': unsafe('<a href="/gods/' + GodsList[i].name.toLowerCase() + '">' + GodsList[i].name + '</a>'),
      'Roman Name': unsafe(GodsList[i].romanname),
      'Symbol': unsafe(GodsList[i].symbol),
      'Power': unsafe(GodsList[i].power),
      'Father': unsafe(GodsList[i].father),
      'Mother': unsafe(GodsList[i].mother)
    };
    godsinfo.push(god);
}

ReactDOM.render(
  <div>
    <Table className="table" id="table" style={{backgroundColor: bgColors.Yellow}}

    data={godsinfo}

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
      'Roman Name',
      'Symbol',
      'Power',
      'Father',
      'Mother'
    ]}

    filterable={['Name', 'Roman Name', 'Symbol', 'Power', 'Father', 'Mother']}

    defaultSort={{column: 'Name', direction: 'asc'}} itemsPerPage={5} pageButtonLimit={100}/>
  </div>,
    document.getElementById('gods')
);
