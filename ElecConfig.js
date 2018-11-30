var formula = ['S', 'S', 'P', 'S', 'P', 'S', 'D', 'P', 'S', 'D', 'P', 'S', 'F', 'D', 'P', 'S', 'F', 'D', 'P', 'S'];
		var partnum = ['1', '2', '2', '3', '3', '4', '3', '4', '5', '4', '5', '6', '4', '5', '6', '7', '5', '6', '7', '8'];
		var protons;
		var result;
		var lastletter;
		var parsedlastletter;
		var simplelastletter;
		var configurate = function() {
      var protons;
			result="";
			i=0;
			parti=0;
			differ=0;
			protons=document.getElementById("atomic_number").value;
			//console.log(protons);
			var i=0;
			var parti=0;
			var differ=0;
			while(i<protons) {
				/*
				console.log(i);
				console.log(parti);
				console.log(formula[i]);
				console.log(result);
				*/

			switch(formula[parti]) {
				case 'S':
					result+=""+partnum[parti]+"S"+2+" ";
					i+=2;
					break;
				case 'P':
					i+=6;
					result+=partnum[parti]+"P"+6+" ";
					break;
				case 'D':
					i+=10;
					result+=partnum[parti]+"D"+10+" ";
					break;
				case 'F':
					i+=14;
					result+=partnum[parti]+"F"+14+" ";
					break;
			}
			parti++;

			}

			if(i>protons) {
				//console.log(i);
				lastletter=result.charAt(result.length-3)+result.charAt(result.length-2);
				//console.log(lastletter);
				parsedlastletter=lastletter.match(/\d+/g).map(Number);
				//console.log(result.length);
				//console.log(parsedlastletter.toString().length);
				//console.log(parsedlastletter);
				//console.log(result);
				result = result.substring(0, result.length - (parsedlastletter.toString().length+1));
				//console.log(result);
				if(parsedlastletter.length===1) {
					simplelastletter=parsedlastletter[0].toString();
				} else if(parsedlastletter.length===2) {
					simplelastletter=parsedlastletter[0].toString() + parsedlastletter[1].toString();
				} else {

				}
				//console.log(simplelastletter);
				differ=parseInt(simplelastletter)-(i-protons);
				//console.log(differ);
				result=result+differ;
			}
			//console.log(result);
			//document.getElementById("result").innerHTML=result;
			return result;
		}
