// var data = Object.values(price_df);
console.log("working?")

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
      // 3. Create a variable that holds the samples array. 
      var tickers = data.Ticker;
      console.log(tickers)
      var closing_price = data.Close;
      // 4. Create a variable that filters the samples for the object with the desired sample number.
      const filteredTicker = Object.fromEntries(
        Object.entries(tickers).filter(([key, val]) => val === newTicker))
      console.log(filteredTicker)

      const filteredClosing = Object.fromEntries(
        Object.entries(closing_price).filter(([key, val]) => val === newTicker))
      console.log(closing_price)
      
      


      //  5. Create a variable that holds the first sample in the array.
      var result = resultArray[0];
      // console.log(result)
      metaDataSample= metaDataArray[0];
      // console.log(metaDataSample)
      // 6. Create variables that hold the otu_ids, otu_labels, and sample_values.
      let wfreq = metaDataSample.wfreq;
      let ids = result.otu_ids;
      let labels = result.otu_labels;
      let values = result.sample_values;
      // console.log(wfreq)
      // console.log(ids.slice(0,10))
      // console.log(values.slice(0,10))
      // console.log(labels)
      // 7. Create the yticks for the bar chart.
      // Hint: Get the the top 10 otu_ids and map them in descending order  
      //  so the otu_ids with the most bacteria are last. 
  
      // var yticks = ids.sort((a,b) => values[a] - values[b]).reverse().slice(0,10)
  
      // var yticks = ids.map(sampleObj => {
      //   otu = "OTU "
      //   return otu + sampleObj
      // }).slice(0,10).reverse()
  
      var yticks = ids.map(sampleObj => "OTU " + sampleObj).slice(0,10).reverse()
     
      // var yticks = ids.slice(0,10)
      // console.log(yticks)
      
  
      
      // 8. Create the trace for the bar chart.
     
      var barData = [{
      x: values.slice(0,10).reverse(),
      y: yticks,
      text: labels.slice(0,10).reverse(),
      type:"bar",
      orientation: "h"
      }];
  
      // 9. Create the layout for the bar chart. 
      var barLayout = {
      title: {
        text: "Top 10 Bacteria Cultures Found",
        font: {
          color: "white"
        }
      },
      plot_bgcolor: "333333",
      paper_bgcolor: "333333",
      font:{
        color: "white"
      }
      };
      // 10. Use Plotly to plot the data with the layout. 
      Plotly.newPlot("bar", barData, barLayout)
  
  
    
    });
}
  
  