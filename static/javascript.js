			function formatSecs(secs) {
				PERMIN = 60;
				PERHOUR = PERMIN*60;
				PERDAY = PERHOUR*24;
				PERYEAR = PERDAY*365;
				PERCENT = PERYEAR*100;

				secs = Math.round(secs);
				output = "" + secs;

				if( secs < PERMIN ) {
					val = secs;
					output = val + ((val == 1) ? " second" : " seconds");
				} else if( secs < PERHOUR ) {
					val = Math.round(secs/PERMIN);
					output = val + ((val == 1) ? " minute" : " minutes");
				} else if( secs < PERDAY ) {
					val = Math.round(secs/PERHOUR);
					output = val + ((val == 1) ? " hour" : " hours");
				} else if( secs < PERYEAR ) {
					val = Math.round(secs/PERDAY);
					output = val + ((val == 1) ? " day" : " days");
				} else if( secs < PERCENT ) {
					val = Math.round(secs/PERYEAR);
					output = val + ((val == 1) ? " year" : " years");
				} else {
					val = Math.round(secs/PERCENT);
					output = val + ((val == 1) ? " century" : " centuries");
				}

				return output;
			}

			function calc(inputArea, outputArea) {
				guessesPerSecond = 1000000;

				specials = "~`!@#$%^&*()-_=+{}[]|\\:;\"'<,>.?/";

				LOWERCASECHAR = 1;
				UPPERCASECHAR = 2;
				NUMBERCHAR = 3;
				SPECIALCHAR = 4;
				possibilitiesPerType = [ 0, 26, 26, 10, specials.length ];

				presTypes = [0];

				pass = document.getElementById(inputArea).value;

				for(i = 0; i < pass.length; i++) {
					if(pass[i] >= "a" && pass[i] <= "z") {
						if(presTypes.indexOf(LOWERCASECHAR) == -1) {
							presTypes = presTypes.concat(LOWERCASECHAR);
						}
					} else if (pass[i] >= "A" && pass[i] <= "Z") {
						if(presTypes.indexOf(UPPERCASECHAR) == -1) {
							presTypes = presTypes.concat(UPPERCASECHAR);
						}
					} else if (pass[i] >= "0" && pass[i] <= "9") {
						if(presTypes.indexOf(NUMBERCHAR) == -1) {
							presTypes = presTypes.concat(NUMBERCHAR);
						}
					} else if ( specials.indexOf(pass[i]) > -1 ) {
						if(presTypes.indexOf(SPECIALCHAR) == -1) {
							presTypes = presTypes.concat(SPECIALCHAR);
						}
					} else {
						//alert("funky char man!");
					}
				}

				possPerChar = presTypes.reduce(
						function (a, b) {return a + possibilitiesPerType[b];});

				iter = Math.pow(possPerChar, pass.length);
				secsReqd = iter/guessesPerSecond;

				document.getElementById(outputArea).innerHTML = formatSecs(secsReqd);
			}

			function rotate(rotation) {
				return function(letter) {
					code = letter.charCodeAt(0);
					retcode = 0;
					a = "a".charCodeAt("0");
					z = "z".charCodeAt("0");
					A = "A".charCodeAt("0");
					Z = "Z".charCodeAt("0");
					c0 = "0".charCodeAt("0");
					c9 = "9".charCodeAt("0");
					if( code >= a && code <= z ) {
						retcode = ((code - a + rotation) % 26) + a;
					} else if( code >= A && code <= Z ) {
						retcode = ((code - A + rotation) % 26) + A;
					} else if( code >= c0 && code <= c9 ) {
						retcode = ((code - c0 + rotation) % 10) + c0;
					} else {
						retcode = code;
					}
					return String.fromCharCode(retcode);
				}
			}

			function caesar(plaintext) {
				output = plaintext.split("").map(rotate(3)).join("");
				document.getElementById("ciphertext").value = output;
			}
