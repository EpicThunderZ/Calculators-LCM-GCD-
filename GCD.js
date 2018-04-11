var NULL="";
var gcd=function(NumOne, NumTwo, STOPinput, BigNum, MiniNum, results, CalcNumOne, CalcNumTwo, BigCheck, CalcNumOneRes, CalcNumTwoRes) {
  console.log("clicked");
  results=[];
  console.log(NumOne+","+NumTwo);
  console.log(NumOne>NumTwo);
  BigCheck=NumOne>NumTwo;
  console.log("BigCheck:");
  console.log(BigCheck);
  console.log(NumOne);
  if(isNaN(NumOne)===true || isNaN(NumTwo)===true || NumOne<0 || NumTwo<0) {
    console.log("You made a mistake while typing input.");
    return "Try Again";
  }

    if(BigCheck===true)  {
      BigNum=NumOne;
      MiniNum=NumTwo;
    } else if(BigCheck===false) {
      BigNum=NumTwo;
      MiniNum=NumOne;
    } else{
      console.log("Error. That's weird! Please tell EpicThunderZ about this.");
      window.alert("Error. That's weird! Please tell EpicThunderZ about this.");
      return "Error. <br>That's weird! Please tell EpicThunderZ about this.";
    }

      CalcNumOne=(BigNum-((parseInt(BigNum/MiniNum))*MiniNum));
      CalcNumTwo=MiniNum;

      results.push("gcd("+BigNum+", "+MiniNum+")");
      results.push("gcd("+CalcNumOne+", "+CalcNumTwo+")");
      console.log(results);

      BigCheck=CalcNumOne>CalcNumTwo;
      console.log("BigCheck:");
      console.log(BigCheck);

      while(CalcNumOne!==0) {

        if(BigCheck===false) {
          CalcNumOneRes=CalcNumOne;
          CalcNumTwoRes=CalcNumTwo;

          CalcNumTwo=CalcNumOneRes;
          CalcNumOne=(CalcNumTwoRes-((parseInt(CalcNumTwoRes/CalcNumOneRes))*CalcNumOneRes));

          console.log(CalcNumOne);
          console.log(CalcNumTwo);

          results.push("GCD("+CalcNumOne+", "+CalcNumTwo+")");
          console.log(results);

        } else {
          console.log("BigCheck is true. That's weird!? Please report this to EpicThunderZ.");
          window.alert("BigCheck is true. That's weird!? Please report this to EpicThunderZ.");
        }
    }
    return CalcNumTwo;

};
