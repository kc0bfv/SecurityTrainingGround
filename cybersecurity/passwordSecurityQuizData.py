passwordSecurity = {
			'title':"Password Security",
			'shortname':"passwords",
			'lessonContentFile':"content/passwordSecurity.html",
			'questions':[
				{
					'question':"What's one purpose of a password?",
					'pointValue':1,
					'answers':[
						{
							'answer':"To make it more difficult to get to websites",
							'correct':False,
							}, # Answer end
						{
							'answer':"To keep other people from seeing your private data",
							'correct':True,
							}, # Answer end
						{
							'answer':"Passwords don't have a purpose",
							'correct':False,
							}, # Answer end
						{
							'answer':"To make it easy to steal money",
							'correct':False,
							}, # Answer end
						], # End of answers
					}, # Question end
				{
					'question':"What's a good way to make a password?",
					'pointValue':1,
					'answers':[
						{
							'answer':"Use 4 random letters, numbers and symbols",
							'correct':False,
							}, # Answer end
						{
							'answer':"Use your username as the password",
							'correct':False,
							}, # Answer end
						{
							'answer':"Use 10 random letters, numbers and symbols",
							'correct':True,
							}, # Answer end
						{
							'answer':"Use your birthday",
							'correct':False,
							}, # Answer end
						], # End of answers
					}, # Question end
				{
					'question':"What's another good way to make a password?",
					'pointValue':1,
					'answers':[
						{
							'answer':"Use your Mom's name",
							'correct':False,
							}, # Answer end
						{
							'answer':"Put 4 or more words together in a phrase you'll remember",
							'correct':True,
							}, # Answer end
						{
							'answer':"Use your real first name followed by your favorite color",
							'correct':False,
							}, # Answer end
						{
							'answer':"Use your dog's name",
							'correct':False,
							}, # Answer end
						], # End of answers
					}, # Question end
				{
					'question':"What's a good tip for passwords?",
					'pointValue':1,
					'answers':[
						{
							'answer':"Use the same password for every website so you only have to remember one",
							'correct':False,
							}, # Answer end
						{
							'answer':"Use one password for websites you don't use often, and that don't store important information.  Use another password for important websites.",
							'correct':False,
							}, # Answer end
						{
							'answer':"Use the website's name as your password",
							'correct':False,
							}, # Answer end
						{
							'answer':"Use a different, difficult to crack, password for every website",
							'correct':True,
							}, # Answer end
						], # End of answers
					}, # Question end
				{
					'question':"What's another good tip for passwords?",
					'pointValue':1,
					'answers':[
						{
							'answer':"Store your passwords using a password storage program, like 1Password or KeePass, so you can have different passwords for each site without forgetting them",
							'correct':True,
							}, # Answer end
						{
							'answer':"Store your passwords on a sheet of paper in your wallet",
							'correct':False,
							}, # Answer end
						{
							'answer':"Store your passwords on a sticky-note on your monitor",
							'correct':False,
							}, # Answer end
						{
							'answer':"Email them to yourself",
							'correct':False,
							}, # Answer end
						], # End of answers
					}, # Question end
				{
					'question':"Which of the following is a good password?  (Here's a difficulty tester...)\
		<div id=\"passwordArea\"> \
			<input type=\"text\" id=\"peBox1\" oninput=\"javascript:calc('peBox1','oaBox1');\"> \
			<label id=\"oaBox1\" for=\"peBox1\">0 seconds</label> \
		</div>",
					'pointValue':1,
					'answers':[
						{
							'answer':"badDog",
							'correct':False,
							}, # Answer end
						{
							'answer':"goofyDogGoesToThePound",
							'correct':True,
							}, # Answer end
						{
							'answer':"12345",
							'correct':False,
							}, # Answer end
						{
							'answer':"qwe123@",
							'correct':False,
							}, # Answer end
						], # End of answers
					}, # Question end
				{
					'question':"Which of the following is a good password for user \"billyJean\"?  (Here's a difficulty tester...)\
		<div id=\"passwordArea\"> \
			<input type=\"text\" id=\"peBox2\" oninput=\"javascript:calc('peBox2','oaBox2');\"> \
			<label id=\"oaBox2\" for=\"peBox2\">0 seconds</label> \
		</div>",
					'pointValue':1,
					'answers':[
						{
							'answer':"billyJean",
							'correct':False,
							}, # Answer end
						{
							'answer':"12345",
							'correct':False,
							}, # Answer end
						{
							'answer':"billyJeanFacebook",
							'correct':False,
							}, # Answer end
						{
							'answer':"en$2m@q4%3nd",
							'correct':True,
							}, # Answer end
						], # End of answers
					}, # Question end
				{
					'question':"Which of the following is a good password for James Smith?  (Here's a difficulty tester...)\
		<div id=\"passwordArea\"> \
			<input type=\"text\" id=\"peBox3\" oninput=\"javascript:calc('peBox3','oaBox3');\"> \
			<label id=\"oaBox3\" for=\"peBox3\">0 seconds</label> \
		</div>",
					'pointValue':1,
					'answers':[
						{
							'answer':"iWouldNotWalk500Miles",
							'correct':True,
							}, # Answer end
						{
							'answer':"james.Smith",
							'correct':False,
							}, # Answer end
						{
							'answer':"12345",
							'correct':False,
							}, # Answer end
						{
							'answer':"ej3#2nf",
							'correct':True,
							}, # Answer end
						], # End of answers
					}, # Question end
				{
					'question':"What technique do hackers use to figure out your password?",
					'pointValue':1,
					'answers':[
						{
							'answer':"Manual guess-and-check, which is also how they do algebra",
							'correct':False,
							}, # Answer end
						{
							'answer':"Cracking, where a computer tries passwords over and over",
							'correct':True,
							}, # Answer end
						{
							'answer':"They can't figure out your password because it's secure",
							'correct':False,
							}, # Answer end
						{
							'answer':"They just press buttons on the keyboard until the computer breaks",
							'correct':False,
							}, # Answer end
						], # End of answers
					}, # Question end
				{
					'question':"What technique do responsible companies use to store passwords?",
					'pointValue':1,
					'answers':[
						{
							'answer':"Hashing, which turns passwords into gobbeldygook",
							'correct':True,
							}, # Answer end
						{
							'answer':"They store the password exactly as you type it",
							'correct':False,
							}, # Answer end
						{
							'answer':"Encryption, which turns passwords into unicorn toots",
							'correct':False,
							}, # Answer end
						{
							'answer':"Post-it notes stuck to their computer monitors",
							'correct':False,
							}, # Answer end
						], # End of answers
					}, # Question end
				], # End of questions
} # Quiz End
