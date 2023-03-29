*{box-sizing: border-box; margin: 0; padding: 0;}
body{background-color: #1d1d1d;}

::selection{background-color: transparent;}

.screen{
	height: 75px;
	width: 225px;
	border-radius: 15px;
	border: 8px solid #2b2b2b;
	background-color: #111;
	font-size: 50px;
	color: limegreen;
	padding: 0px 20px 0px 20px;
	letter-spacing: 26px;
	font-family: 'VT323', monospace;
	position: relative;
}

.notification{
	color: limegreen;
	font-family: 'VT323', monospace;
	text-align: center;
	font-size: 40px;
	position: absolute;
	width: 225px;
	top: 15px;
	display: none;
}


@keyframes blink {
	0%{opacity: 0;}
	50%{opacity: 1;}
	100%{opacity: 0;}
}
@-webkit-keyframes blink {
	0%{opacity: 0;}
	50%{opacity: 1;}
	100%{opacity: 0;}
}