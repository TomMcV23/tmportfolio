const fs = require('fs');

module.exports = {

   // Exercise 1
   freefall: (val, isD) => {
    //If isD is true then the calculation to find the time is carried out
    if (isD == true) {
    form = ((2*val/9.81)**(1/2));
    } 
    //Otherwise the calculation to find the distance is carried out
    else {
    form = ((1/2)*9.81*(val**2));
    }
//The result of which ever calculation that was carried out is then returned to two decimal placesc
return(form.toFixed(2));
},

// Exercise 2 
RPS: (play) => {
    // identify variables
    rpsstr = play
    rpsres = "" 
    len = play.length
    // for loop that starts with l at 0 then incriments to search through the input strings
    // upon finding a letter that matches l incriments by 1 and changes the letter in question to 
    // to what it needs to be
    for (var l = 0; l < len; l++) {
        if(rpsstr.charAt(l) == "R") {
            rpsres += ("P");
          }
        else if(rpsstr.charAt(l) == "P") {
            rpsres += ("S");
          }
        else if(rpsstr.charAt(l) == "S") {
          rpsres += ("R");
          } 
        }
// return the result of the for loop
return rpsres
},
// Exercise 3
list2str: (l) => {
    // converts the list to string
    l = JSON.stringify(l);
    // replaces punctuation
    l = l.replace(/,/g,"").replace(/"/g,"")
    return l;
},

// Exercise 4
textPreprocessing: (text) => {
    var text;
    // take the text and remove the punctuation 
    ptext = text.replace(".","").replace("?","").replace(/!/g,"").replace(/,/g,"").replace(/:/g,"").replace(/;/g,"").replace(/-/g,"").replace("[","").replace("]","").replace("{","").replace("}","").replace("(","").replace(")","");
    // stem the words 
    stext = ptext.replace(/s+\s/g, " ").replace("ing","").replace("ed","")
    // make the text lowercase
    ltext = stext.toLowerCase();
    // declare the list of stop words to be removed
    const stopwords = ["i","a","about","am","an","are","as","at","be","by","for","from","how","in","is","it","of","on","or","that","the","this","to","was","what","when","where","who","will","with","i"];
    //convert the text in to a list
    lst = ltext.split(" ");
    // take the input of the list and filter through looking for the words to be removed and remove them
    // this code was taken from reddit from the user __mak
    //accessed on 18/11/2021
    //available from https://www.reddit.com/r/javascript/comments/2g0oxj/how_do_i_remove_from_an_array_those_elements_that/
    // it is the second comment on the thread
    var res = lst.filter(function(element){
        return stopwords.indexOf(element) === -1;
    }); 
    // end of referenced code
    // return the result
    return res;
},

// Exercise 5
isGreaterThan: (dict1, dict2) => {
   // declare key variables for each dictionary
    let key1 = Object.getOwnPropertyNames(dict1);
    let key2 = Object.getOwnPropertyNames(dict2);
    // check the length of each value to see if key 1 is greater than the other
    if (key1.length >= key2.length) {
        return false;
    }
    // check through each value in key1 
    for (let i = 0; i < key1.length; i++) {
        let key = key1[i];
        //check the value of dict 1 keys to see if they are greater than dict 2 keys
        if (dict1[key] >= dict2[key]) {
            return false;
        }
    }
    return true;
},

// Exercise 6
CSVsum: (filename) => {
    var data  = fs.readFileSync(filename);
    data = data.split("\r\n");
},

// Exercise 7
str2list: (s) => {
    //string = s.replace(/]/g,"").replace("[", "");
    //text = string.split("[").filter(Boolean).map(substr => substr.split(""));
    //return string.split("")
    let lst = s.split("");
    for (let i = 0; i < lst.length; i++) {
        q = "["
        q = q.replace(/"/, "")
        w = "]"
        w = w.replace(/"/, "")
        if (lst[i] == "[") {
                lst[i] = /\[/; //"\u00a5 uni code no work 
        }
            else if  (lst[i] == "]"){
                lst[i] = /\]/;//FIND OUT HOW TO TURN TO BRACKET
            } 
    }
    return lst
},

// Exercise 8
spacemonSim: (roster1, roster2) => {
    return undefined;
},

// Exercise 9
rewardShortPath: (env) => {
    return undefined;
},

// Exercise 10
cliqueCounter: (network) => {
    return undefined;
}
}
