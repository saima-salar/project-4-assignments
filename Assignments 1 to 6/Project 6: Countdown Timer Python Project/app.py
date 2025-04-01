import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)  # Calculate minutes and seconds
        time_format = '{:02d}:{:02d}'.format(mins, secs)  # MM:SS format
        print(f"\r⏳ Countdown: {time_format}", end="")  # Display countdown in the same line
        time.sleep(1)  # Delay for 1 second
        seconds -= 1

    print("\n⏰ 00:00 - Time's Up! 🎉")  # Timer end message

# User input for timer
try:
    total_seconds = int(input("⏱️ Enter time in seconds for countdown: "))
    countdown_timer(total_seconds)
except ValueError:
    print("⚠️ Please enter a valid number!")

