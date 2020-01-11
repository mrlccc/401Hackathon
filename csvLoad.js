//Load all csv data into globalData synchronously

let loaded = false;
let globalData;
d3.csv("./netflix_titles_nov_2019.csv").then(function(data) {
    loaded = true;
    globalData = data;
    console.log("Done");
  });
while(!loaded){}


