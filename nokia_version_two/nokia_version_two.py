opinion = True

while(opinion):
	nokia_manual = """

	1. PhoneBook
	2. Messages
	3. Chat
	4. Call Register
	5. Tones
	6. Settings
	7. Call divert
	8. Music
	9. Games
	10. Calculator
	11. Reminders
	12. Clocks
	13. Profile
	14. Services
	15. SIM services
	 0. Back

	"""

	print(nokia_manual)

	menu_functions_no = int(input("Enter number: "))

	match menu_functions_no:
	    case 1:
	        print("PhoneBook")

	        opinion_phonebook = True
	        while(opinion_phonebook):

		        phone_book_menus = """

		        1 Search
		        2 Service no
		        3 Add name
		        4 Erase
		        5 Edit
		        6 Copy
		        7 Assign tone
		        8 Send b'card
		        9 Options
		        10 Speed dials
		        11 Voice tags
		         0 Back

		        """

		        print(phone_book_menus)

		        phone_book_menus_no = int(input("Enter: "))


		        match phone_book_menus_no:

		        	case 1:
		        		print("Search")
		        	case 2:
		        		print("Service no")
		        	case 3:
		        		print("Add name")
		        	case 4:
		        		print("Erase")
		        	case 5:
		        		print("Edit")
		        	case 6:
		        		print("Copy")
		        	case 7:
		        		print("Assign tone")
		        	case 8:
		        		print("Send b'card")
		        	case 9:
		        		print("Options")

		        		opinion_option = True
		        		while(opinion_option):

		        			options_menu = """

		        		1 Memory in use
		        		2 Type of view
		        		3 Memory status
		        		0 Back
		        			""" 

		        			print(options_menu)

		        			options_menu_no = int(input("Enter number: "))

		        			match options_menu_no:
		        				case 1:
		        					print("Memory in use")
		        				case 2:
		        					print("Type of view")
		        				case 3:
		        					print("Memory status")
		        				case 0:
		        					opinion_option = False
		        				case _:
		        					print("Not valid")

		        	case 10:
		        		print("Speed dials")
		        	case 11:
		        		print("Voice tags")
		        	case 0:
		        		opinion_phonebook = False
		        	case _:
		        		print("Not valid")



	    case 2:
	        print("Messages")

	        opinion_messages = True
	        while(opinion_messages):

		        menu_messages = """

		        1 Write messages
		        2 Inbox
		        3 Outbox
		        4 Picture messages
		        5 Templates
		        6 Smileys
		        7 Message settings
		        8 Info service
		        9 Voice mailbox number
		        10 Service command editor
		         0 Back

		        """

	        	print(menu_messages)

	        	menu_messages_no = int(input("Enter number: "))

		        match menu_messages_no:

		        	case 1:
		        		print("Write messages")
		        	case 2:
		        		print("Inbox")
		        	case 3:
		        		print("Outbox")
		        	case 4:
		        		print("Picture messages")
		        	case 5:
		        		print("Templates")
		        	case 6:
		        		print("Smileys")
		        	case 7:
		        		print("Message settings")

		        		opinion_message_setting = True

		        		while opinion_message_setting:
		        			message_settings_menu = """

			        		1 Set
			        		2 Common
			        		0 Back

			        		"""

		        			print(message_settings_menu)

		        			message_settings_no = int(input("Enter number: "))

		        			match message_settings_no:

			        			case 1:
			        				print("Set")

			        				opinion_sets_menu = True

			        				while opinion_sets_menu:
				        				sets_menu = """

				        				1 Message center number
				        				2 Message sent as
				        				3 Message validity
				        				0 Back

				        				"""
				        				print(sets_menu)

				        				menu_for_sets = int(input("Enter number"))
				        				match menu_for_sets:
				        					case 1:
				        						print("Message center number")
				        					case 2:
				        						print("Message sent as")
				        					case 3:
				        						print("Message validity")
				        					case 0:
				        						opinion_sets_menu = False
				        					case _:
				        						print("Not valid")

			        			case 2:
			        				print("Common")
			        			case 0:
			        				opinion_message_setting = False
			        			case _:
			        				print("Not valid")


		        	case 8:
		        		print("Info service")
		        	case 9:
		        		print("Voice mailbox number")
		        	case 10:
		        		print("Service command editor")
		        	case 0:
		        		opinion_messages = False
		        	case _:
		        		print("Not valid")
	    case 3:
	        print("Chat")
	    case 4:
	        print("Call Register")

	        opinion_call_registers = True
	        while(opinion_call_registers):

		        menu_call_register = """

		        1 Missed calls
		        2 Received calls
		        3 Dialled number 
		        4 Erase recent call lists
		        5 Show call duration
		        6 Show call costs
		        7 Call cost settings
		        8 Prepaid credit
		        0 Back

	        	"""

	        	print(menu_call_register)

	        	menu_call_register_no = int(input("Enter number: "))

		        match menu_call_register_no:
		        	case 1:
		        		print("Missed calls")
		        	case 2:
		        		print("Received calls")
		        	case 3:
		        		print("Dialled number")
		        	case 4:
		        		print("Erase recent call lists")
		        	case 5:
		        		print("Show call duration")

		        		opinion_menu_show = True

		        		while opinion_menu_show:
			        		menu_show_call_duration = """

			        		1 Last call duration
			        		2 All calls duration
			        		3 Received calls' duration
			        		4 Dialled calls' duration
			        		5 Clear timers
			        		0 Back

			        		"""

		        			print(menu_show_call_duration)

		        			call_duration = int(input("Enter number: "))

		        			match call_duration:
			        			case 1:
			        				print("Last call duration")
			        			case 2:
			        				print("All calls duration")
			        			case 3:
			        				print("Received calls' duration")
			        			case 4:
			        				print("Dialled calls duration")
			        			case 5:
			        				print("Clear timers")
			        			case 0:
			        				opinion_menu_show = False
			        			case _:
			        				print("Not valid")

		        	case 6:
		        		print("Show call costs")

		        		opinion_menu_show_call = True

		        		while opinion_menu_show_call:
			        		menu_show_call_cost = """

			        		1 Last call cost
			        		2 All calls' cost
			        		3 Clear counters
			        		0 Back

			        		"""

			        		print(menu_show_call_cost)
			        		show_call_cost_index = int(input("Enter number: "))
			        		match show_call_cost_index:
			        			case 1:
			        				print("Last call cost")
			        			case 2:
			        				print("All calls' cost")
			        			case 3:
			        				print("Clear counters")
			        			case 0:
			        				opinion_menu_show_call = False
			        			case _:
			        				print("Not valid")
		        	case 7:
		        		print("Call cost settings")

		        		opinion_call_cost = True

		        		while opinion_call_cost:

			        		menu_call_cost = """

			        		1 Call cost limit
			        		2 Show costs in
			        		0 Back

			        		"""

			        		print(menu_call_cost)

			        		menu_call_cost_no = int(input("Enter number: "))

			        		match menu_call_cost_no:
			        			case 1:
			        				print("Call cost limit")
			        			case 2:
			        				print("Show costs in")
			        			case 0:
			        				opinion_call_cost = False
			        			case _:
			        				print("Not valid")


		        	case 8:
		        		print("Prepaid credit")
		        	case 0:
		        		opinion_call_registers = False
		        	case _:
		        		print("Not valid")
	    case 5:
	        print("Tones")
	    case 6:
	        print("Settings")

	        opinion_menu_settings = True

	        while opinion_menu_settings:

		        menu_settings = """

		        1 Call settings
		        2 Phone settings
		        3 Security settings
		        4 Restore factory settings
		        0 Back
		        
		        """

	        	print(menu_settings)

	        	settings_no = int(input("Enter number: "))

	        	match settings_no:
		        	case 1:
		        		print("Call settings")

		        		opinion_menu_call_settings = True

		        		while opinion_menu_call_settings:

			        		menu_call_settings = """

			        		1 Automatic redial
			        		2 Speed learning
			        		3 Call waiting options
			        		4 Own number sending
			        		5 Phone line in use
			        		6 Automatic answer
			        		0 Back

			        		"""

			        		print(menu_call_settings)

			        		menu_call_settings_no = int(input("Enter number: "))

			        		match menu_call_settings_no:
			        			case 1:
			        				print("Automatic redial")
			        			case 2:
			        				print("Speed learning")
			        			case 3:
			        				print("Call waiting options")
			        			case 4:
			        				print("Own number sending")
			        			case 5:
			        				print("Phone line in use")
			        			case 6:
			        				print("Automatic answer")
			        			case 0:
			        				opinion_menu_call_settings = False
			        			case _:
			        				print("Not valid")


		        	case 2:
		        		print("Phone settings")

		        		opinion_menu_phone_settings = True

		        		while opinion_menu_phone_settings:

			        		menu_phone_settings = """

			        		1 Language
			        		2 Cell info display
			        		3 Welcome note
			        		4 Network selection
			        		5 Confirm SIM service actions
			        		0 Back

			        		"""

			        		print(menu_phone_settings)

			        		phone_settings_no = int(input("Enter number: "))

			        		match phone_settings_no:
			        			case 1:
			        				print("Language")
			        			case 2:
			        				print("Cell info display")
			        			case 3:
			        				print("Welcome note")
			        			case 4:
			        				print("Network selection")
			        			case 5:
			        				print("Confirm SIM service actions")
			        			case 0:
			        				opinion_menu_phone_settings = False
			        			case _:
			        				print("Not valid")
		        	case 3:
		        		print("Security settings")

		        		opinion_menu_security_settings = True

		        		while opinion_menu_security_settings:

			        		menu_security_settings = """

			        		1 PIN code 
			        		2 Call barring service
			        		3 Fixed dialling 
			        		4 Closed user group
			        		5 Security level
			        		6 Change access codes
			        		0 Back

			        		"""

			        		print(menu_security_settings)

			        		menu_security_settings_no = int(input("Enter Number: "))

			        		match menu_security_settings_no:
			        			case 1:
			        				print("PIN code")
			        			case 2:
			        				print("Call barring service")
			        			case 3:
			        				print("Fixed dialling")
			        			case 4:
			        				print("Closed user group")
			        			case 5:
			        				print("Security level")
			        			case 6:
			        				print("Change access codes")
			        			case 0:
			        				opinion_menu_security_settings = False
			        			case _:
			        				print("Not valid")



		        	case 4:
		        		print("Restore factory settings")
		        	case 0:
		        		opinion_menu_settings = False
		        	case _:
		        		print("Not valid")

	    case 7:
	        print("Call divert")
	    case 8:
	        print("Music")

	        opinion_menu_music = True
	        while(opinion_menu_music):

		        menu_music = """

		        1 Music player
		        2 Radio
		        3 Recorder 
		        4 Track list
		        0 Back

	        """
		        print(menu_music)

		        menu_music_no = int(input("Enter number: "))

		        match menu_music_no:
		        	case 1:
		        		print("Music player")
		        	case 2:
		        		print("Radio")
		        	case 3:
		        		print("Recorder")
		        	case 4:
		        		print("Track list")
		        	case 0:
		        		opinion_menu_music = False
		        	case _:
		        		print("Not valid")

	    case 9:
	        print("Games")
	    case 10:
	        print("Calculator")
	    case 11:
	        print("Reminders")
	    case 12:
	        print("Clocks")

	        opinion_clocks = True
	        while(opinion_clocks):

		        menu_clocks = """

		        1 Alarm clock
		        2 Clock settings
		        3 Date settings
		        4 Stopswatch 
		        5 Countdown timer
		        6 Auto update of date and time
		        0 Back

	        """

	        	print(menu_clocks)

	        	menu_clocks_no = int(input("Enter number: "))

		        match menu_clocks_no:
		        	case 1:
		        		print("Alarm clock")
		        	case 2:
		        		print("Clock settings")
		        	case 3:
		        		print("Date settings")
		        	case 4:
		        		print("Stopswatch")
		        	case 5:
		        		print("Countdown timer")
		        	case 6:
		        		print("Auto update of date and time")
		        	case 0:
		        		opinion_clocks = False
		        	case _:
		        		print("Not valid")

	    case 13:
	        print("Profiles")
	    case 14:
	        print("Services")
	    case 15:
	        print("SIM services")
	    case 0:
	    	opinion = False
	    case _:
	        print("Not valid")






























