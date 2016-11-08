var Table = Reactable.Table,
    unsafe = Reactable.unsafe;

var bgColors = { "Default": "#81b71a",
                    "Blue": "#00B1E1",
                    "Cyan": "#37BC9B",
                    "Green": "#8CC152",
                    "Red": "#E9573F",
                    "Yellow": "#F6BB42",
};

ReactDOM.render(
  <div>
    <Table className="table" id="table" style={{backgroundColor: bgColors.Yellow}} data={[
        {
          'Name': unsafe('<a href="/gods/zeus">Zeus</a>'),
          'Power': unsafe("Sky, weather, kings, fate"),
          'Parents': unsafe("Kronos and Rhea"),
          'Olympian': unsafe("yes"),
          'Children': unsafe("Aphrodite, Phersephone, Hercules"),
          'Symbol': unsafe("Lightning bolt, eagle, bull"),
          'Counterpart': unsafe("Jupiter")
        },
        {
          'Name': unsafe('<a href="/gods/poseidon">Poseidon</a>'),
          'Power': unsafe("King of the Sea, earthquakes, floods, horses"),
          'Parents': unsafe("Kronos and Rhea"),
          'Olympian': unsafe("yes"),
          'Children': unsafe("Triton, Nerids"),
          'Symbol': unsafe("Trident, Bull, horse, dolphin"),
          'Counterpart': unsafe("Neptune")
        },
        {
          'Name': unsafe('<a href="/gods/hades">Hades</a>'),
          'Power': unsafe("God of the dead, king of the underworld"),
          'Parents': unsafe("Kronos and Rhea"),
          'Olympian': unsafe("yes"),
          'Children': unsafe("Cerberus, the Erinyes"),
          'Symbol': unsafe("Royal sceptre, cornucopia"),
          'Counterpart': unsafe("Pluto")
        },
    ]}
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
      'Power',
      'Parents',
      'Olympian',
      'Children',
      'Symbol',
      'Counterpart'
    ]}

    filterable={['Name', 'Power']}

    defaultSort={{column: 'Name', direction: 'asc'}} itemsPerPage={2} pageButtonLimit={5}/>
  </div>,
    document.getElementById('gods')
);
