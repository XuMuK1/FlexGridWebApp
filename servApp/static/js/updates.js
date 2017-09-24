function updateClock ( )
	{
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

function updateArduino ( )
	{
		
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
				housesData=result.split(",")
				
				for(i=0;i<housesData.length;i++){              //4 is the number of desired measurements
					document.getElementById("house"+(Math.floor(i/4)+1)+"_"+( (i%4) +1)).firstChild.nodeValue =  housesData[i];
				}
    			},
			error: function(error) {
        			console.log("Error in UpdateArduino request: "+error.toString());
			}

		});
		

	}