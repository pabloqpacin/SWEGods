// console.log(s.name);
//
// ReactDOM.render(
//     <p>HELLLO</p>,
//     document.getElementById('gods')
// );

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

var godsinfoand = [];
for (var i = 0; i < GodsList.length; i++) {
    var god = {
      'Name': unsafe('<a href="/gods/' + GodsList[i].name.toLowerCase() + '">' + GodsList[i].name + '</a>'),
      'Roman Name': unsafe(GodsList[i].romanname),
      'Symbol': unsafe(GodsList[i].symbol),
      'Power': unsafe(GodsList[i].power),
      'Father': unsafe(GodsList[i].father),
      'Mother': unsafe(GodsList[i].mother)
    };
    godsinfoand.push(god);
}

var heroesinfoand = [];
for (var i = 0; i < HeroesList.length; i++) {
    var hero = {
      'Name': unsafe('<a href="/heroes/' + HeroesList[i].name.toLowerCase() + '">' + HeroesList[i].name + '</a>'),
      'Type': unsafe(HeroesList[i].hero_type),
      'Power': unsafe(HeroesList[i].power),
      'Home': unsafe(HeroesList[i].home),
      'Father': unsafe(HeroesList[i].father),
      'Mother': unsafe(HeroesList[i].mother)
    };
    heroesinfoand.push(hero);
}

var locationsinfoand = [];
for (var i = 0; i < LocationsList.length; i++) {
    var location = {
      'Name': unsafe('<a href="/locations/' + LocationsList[i].name.toLowerCase() + '">' + LocationsList[i].name + '</a>'),
      'Alternate Name': unsafe(LocationsList[i].altname),
      'Type': unsafe(LocationsList[i].location_type),
      'Myth': unsafe(LocationsList[i].myth),
      'Characters': unsafe(LocationsList[i].gods)
    };
    locationsinfoand.push(location);
}

var mythsinfoand = [];
for (var i = 0; i < MythsList.length; i++) {
    var myth = {
      'Name': unsafe('<a href="/myths/' + MythsList[i].name.toLowerCase() + '">' + MythsList[i].name + '</a>'),
      'Description': unsafe(MythsList[i].description),
      'Theme': unsafe(MythsList[i].theme),
      'Place': unsafe(MythsList[i].place),
      'Gods': unsafe(MythsList[i].gods),
      'Characters': unsafe(MythsList[i].characters)
    };
    mythsinfoand.push(myth);
}

var godsinfoor = [];
for (var i = 0; i < GodsList.length; i++) {
    var god = {
      'Name': unsafe('<a href="/gods/' + GodsList[i].name.toLowerCase() + '">' + GodsList[i].name + '</a>'),
      'Roman Name': unsafe(GodsList[i].romanname),
      'Symbol': unsafe(GodsList[i].symbol),
      'Power': unsafe(GodsList[i].power),
      'Father': unsafe(GodsList[i].father),
      'Mother': unsafe(GodsList[i].mother)
    };
    godsinfoor.push(god);
}

var heroesinfoor = [];
for (var i = 0; i < HeroesList.length; i++) {
    var hero = {
      'Name': unsafe('<a href="/heroes/' + HeroesList[i].name.toLowerCase() + '">' + HeroesList[i].name + '</a>'),
      'Type': unsafe(HeroesList[i].hero_type),
      'Power': unsafe(HeroesList[i].power),
      'Home': unsafe(HeroesList[i].home),
      'Father': unsafe(HeroesList[i].father),
      'Mother': unsafe(HeroesList[i].mother)
    };
    heroesinfoor.push(hero);
}

var locationsinfoor = [];
for (var i = 0; i < LocationsList.length; i++) {
    var location = {
      'Name': unsafe('<a href="/locations/' + LocationsList[i].name.toLowerCase() + '">' + LocationsList[i].name + '</a>'),
      'Alternate Name': unsafe(LocationsList[i].altname),
      'Type': unsafe(LocationsList[i].location_type),
      'Myth': unsafe(LocationsList[i].myth),
      'Characters': unsafe(LocationsList[i].gods)
    };
    locationsinfoor.push(location);
}

var mythsinfoor = [];
for (var i = 0; i < MythsList.length; i++) {
    var myth = {
      'Name': unsafe('<a href="/myths/' + MythsList[i].name.toLowerCase() + '">' + MythsList[i].name + '</a>'),
      'Description': unsafe(MythsList[i].description),
      'Theme': unsafe(MythsList[i].theme),
      'Place': unsafe(MythsList[i].place),
      'Gods': unsafe(MythsList[i].gods),
      'Characters': unsafe(MythsList[i].characters)
    };
    mythsinfoor.push(myth);
}

ReactDOM.render(
  <div>
    <h3>AND RESULTS</h3>
    <h4>Gods</h4>
    <div>
      <Table className="table" id="table" style={{backgroundColor: bgColors.Yellow}}

      data={godsinfoand}

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

      defaultSort={{column: 'Name', direction: 'asc'}} itemsPerPage={8} pageButtonLimit={100}/>
    </div>
    <h4>Heroes</h4>
    <div>
      <Table className="table" id="table" style={{backgroundColor: bgColors.Yellow}}

      data={heroesinfoand}

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
    </div>
    <h4>Locations</h4>
    <div>
      <Table className="table" id="table" style={{backgroundColor: bgColors.Yellow}}

      data={locationsinfoand}

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
    </div>
    <h4>Myths</h4>
    <div>
      <Table className="table" id="table" style={{backgroundColor: bgColors.Yellow}}

      data={mythsinfoand}

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
        'Description',
        'Theme',
        'Place',
        'Gods',
        'Characters'
      ]}

      filterable={['Name', 'Description', 'Theme', 'Place', 'Gods', 'Characters']}

      defaultSort={{column: 'Name', direction: 'asc'}} itemsPerPage={3} pageButtonLimit={100}/>
    </div>
    <h3>OR RESULTS</h3>
    <h4>Gods</h4>
    <div>
      <Table className="table" id="table" style={{backgroundColor: bgColors.Yellow}}

      data={godsinfoor}

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

      defaultSort={{column: 'Name', direction: 'asc'}} itemsPerPage={8} pageButtonLimit={100}/>
    </div>
    <h4>Heroes</h4>
    <div>
      <Table className="table" id="table" style={{backgroundColor: bgColors.Yellow}}

      data={heroesinfoor}

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
    </div>
    <h4>Locations</h4>
    <div>
      <Table className="table" id="table" style={{backgroundColor: bgColors.Yellow}}

      data={locationsinfoor}

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
    </div>
    <h4>Myths</h4>
    <div>
      <Table className="table" id="table" style={{backgroundColor: bgColors.Yellow}}

      data={mythsinfoor}

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
        'Description',
        'Theme',
        'Place',
        'Gods',
        'Characters'
      ]}

      filterable={['Name', 'Description', 'Theme', 'Place', 'Gods', 'Characters']}

      defaultSort={{column: 'Name', direction: 'asc'}} itemsPerPage={3} pageButtonLimit={100}/>
    </div>
  </div>,
    document.getElementById('search')
);
