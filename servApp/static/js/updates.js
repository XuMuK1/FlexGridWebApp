function updateClock ( ){
	  	var currentTime = new Date ( );

		  var currentHours = currentTime.getHours ( );
		  var currentMinutes = currentTime.getMinutes ( );
		  var currentSeconds = currentTime.getSeconds ( );

	  // Pad the minutes and seconds with leading zeros, if required
		  currentMinutes = ( currentMinutes < 10 ? "0" : "" ) + currentMinutes;
	
	  // Choose either "AM" or "PM" as appropriate
		  var timeOfDay = ( currentHours < 12 ) ? "AM" : "PM";
	
	  // Convert the hours component to 12-hour format if needed
		  currentHours = ( currentHours > 12 ) ? currentHours - 12 : currentHours;
	
			  // Convert an hours component of "0" to "12"
		  currentHours = ( currentHours == 0 ) ? 12 : currentHours;
	
		  // Compose the string for display
		var currentTimeString = currentTime.getDate()+"."+(currentTime.getMonth()+1)+"."+currentTime.getFullYear()+"  and time is "+currentHours + ":" + currentMinutes + timeOfDay;

		  // Update the time display
		
		
  		document.getElementById("liveClock").firstChild.nodeValue = currentTimeString;
	}

function updateChart(data, index, feature){
	var context=document.getElementById("house"+(index+1)+"_"+feature).getContext("2d");
	
	var steps=1;
	var start=1;
	var step=1;	
	if(feature=="energyExport"){
		step=0.3;
		steps=10;
		start=0;
	}
	//alert("house"+(index+1)+"_"+feature);
	var chart = new Chart(context, {
	// The type of chart we want to create
		    type: 'line',
        	    // The data for our dataset
		    data: {
		        labels: data[index]["timestamps"],
		        datasets: [{
		                label: feature,
				backgroundColor: 'rgba(0,0,0,0)',
	        	        borderColor: 'rgb(255, 99, 132)',
		                data: data[index][feature]
		        }]
		    },
                    // Configuration options go here
		    options: { 
			animation: false,
			maintainAspectRatio: false,
			responsive: true,
			legend: {display: false},
			title: {display: true, text: feature},
			scaleOverride : true,
        		scaleSteps : 10,
        		scaleStepWidth : 50,
        		scaleStartValue : 0 

		    }                    
	});
	

}

function updateArduino ( ){
		
		housesData = [] ;
		
		//alert("JSON!"+JSON.stringify({"command":"UpdateArduino"});		
	  	$.ajax({
    			type : "POST",
    			url : "/",
			data: '{"command":"UpdateArduino"}',
    			contentType: 'application/json;charset=UTF-8',
    			success: function(result) {
        			console.log(result);
				console.log("UPDATING info in table...");
				console.log("REDRAWING realtime charts");
				console.log("UPLOADING info to storages (on server side)");				
				housesData=JSON.parse(result);
				//alert("LENGTH"+housesData.length);				
				for(i=0;i<housesData.length;i++){              //4 is the number of desired measurements
					//alert(i);
					updateChart(housesData,i,"innerConsumption");
					updateChart(housesData,i,"energyExport");
					//updateChart(housesData,i,"budget");
					updateChart(housesData,i,"energyImport");


					//old setting
					//document.getElementById("house"+(Math.floor(i/4)+1)+"_"+( (i%4) +1)).firstChild.nodeValue =  housesData[i];
				}
    			},
			error: function(error) {
        			console.log("Error in UpdateArduino request: "+error.toString());
			}

		});
		

	}

function switchHouse(houseId){
	$.ajax({
    			type : "POST",
    			url : "/",
			data: '{"command":"SwitchHouse","id":'+(houseId-1)+'}',
    			contentType: 'application/json;charset=UTF-8',
    			success: function(result) {
        			console.log(result);
				if(result=="Off"){
					var but=document.getElementById("switchHouse"+houseId);
					but.classList.remove('houseButtonOn');
                                        but.classList.add('houseButtonOff');
					but.innerHTML="Off";					
				}else{
					var but=document.getElementById("switchHouse"+houseId);
					but.classList.remove('houseButtonOff');
                                        but.classList.add('houseButtonOn');
					but.innerHTML="On";
				}
    			},
			error: function(error) {
        			console.log("Error in SwitchHouse request: "+error.toString());
			}

		});
}