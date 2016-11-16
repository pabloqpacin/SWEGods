console.log(HeroesList);

var Table = Reactable.Table,
    unsafe = Reactable.unsafe;

var bgColors = { "Default": "#81b71a",
                    "Blue": "#00B1E1",
                    "Cyan": "#37BC9B",
                    "Green": "#8CC152",
                    "Red": "#E9573F",
                    "Yellow": "#F6BB42",
};

var heroesinfo = [];
for (var i = 0; i < HeroesList.length; i++) {
    var hero = {
      'Name': unsafe('<a href="/heroes/' + HeroesList[i].name.toLowerCase() + '">' + HeroesList[i].name + '</a>'),
      'Type': unsafe(HeroesList[i].hero_type),
      'Power': unsafe(HeroesList[i].power),
      'Home': unsafe(HeroesList[i].home),
      'Father': unsafe(HeroesList[i].father),
      'Mother': unsafe(HeroesList[i].mother)
    };
    heroesinfo.push(hero);
}

ReactDOM.render(
  <div>
    <Table className="table" id="table" style={{backgroundColor: bgColors.Yellow}}

    data={heroesinfo}

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
      'Type',
      'Power',
      'Home',
      'Father',
      'Mother'
    ]}

    filterable={['Name', 'Type', 'Power', 'Home', 'Father', 'Mother']}

    defaultSort={{column: 'Name', direction: 'asc'}} itemsPerPage={8} pageButtonLimit={100}/>
  </div>,
    document.getElementById('heroes')
);
