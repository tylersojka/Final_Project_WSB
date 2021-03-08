// var data = Object.values(price_df);
console.log("working?")
// var test = JSON.parse(document.getElementById("mydatadiv").dataset.test);
// console.log(test)


function init() {
    // Grab a reference to the dropdown select element
    
    


    var selector = d3.select("#dropOptions");
    // Use the list of tickers to populate the select options
    Promise.all([
        d3.json("../../Data/tickerlist.json"),
        d3.json("../../Data/price_mentions.json")
    ]).then(([ticker, data]) => {
        console.log(data)
      var ticker = ticker.Tickers;
        // console.log(ticker)
          

      Object.keys(ticker).forEach((key) => {
        //   console.log(ticker[key])
    // jquery selector append a tag with the data value = to the ticker and a divider line
        $('.dropdown-menu').append(`<a data-value="${ticker[key]}" class="dropdown-item">${ticker[key]}</a> <div class="dropdown-divider"></div>`)
  
      });

  // jquery selector function, on click of a number in dropdown bar, run the option changed function with the value selected.
      $('.dropdown-menu a').click(function(){
      let ticker = $(this).attr('data-value')
      $("#navbarDropdown").text("Stock: " + $(this).attr('data-value'));
      optionChanged(ticker)
      console.log(ticker)
      });
  // for the search form, prevent reloading the page and set the search value = to the input and call option changed function
      $(`#searchForm`).submit(function(e){
        e.preventDefault();
        let searchValue = $(`#searchInput`).val()
        optionChanged(searchValue)
        console.log(searchValue)
      })
  
      // Use the first sample from the list to build the initial plots
      var firstSample = ticker[0];
      buildCharts(firstSample);
      $("#navbarDropdown").text("Subject Number: " + firstSample);
    });
  }
  
  // Initialize the dashboard
  init();


  function optionChanged(newTicker) {
    // Fetch new data each time a new sample is selected
    // buildMetadata(newSample);
    buildCharts(newTicker);
    
  }


  function buildCharts(newTicker) {
  // 2. Use d3.json to load and retrieve the samples.json file 
  d3.json("../../Data/price_mentions.json").then((data) => {

    console.log(data)



  });
}

function makeChart(players) {
    // players is an array of objects where each object is something like:
    // {
    //   "Name": "Steffi Graf",
    //   "Weeks": "377",
    //   "Gender": "Female"
    // }
  console.log(players.Close)
    var playerLabels = players.map(function(d) {
      return d.Ticker;
    });
   
    var weeksData = players.map(function(d) {
      return +d.date;
    });
  
    var lineChartSecond = new Chart('lineChartSecond', {
      type: "horizontalBar",
      options: {
        maintainAspectRatio: true,
        legend: {
          display: true
        }
      },
      data: {
        labels: playerLabels,
        datasets: [
          {
            data: weeksData
          }
        ]
      }
    });
  }
  
  // Request data using D3
