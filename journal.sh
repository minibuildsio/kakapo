#!/bin/bash

function usage() {
  echo "Usage:"
  echo "  journal [OPTION] [ENTRY TEXT]"
  echo ""
  echo "  -d      date of the journal entry defaults to today"
  echo ""
  echo "Examples:"
  echo "  journal"
  echo "  journal -d \"2022-07-01\""
  echo "  journal \"Entry text\""
  echo "  journal -d \"last monday\" \"Entry text\""
}

while getopts hd: option
do
  case $option in
    d) date_in=$OPTARG;;
    h | *) 
      usage
      exit 0
    ;;
  esac
done

date=$(date -d "${date_in:-"$(date)"}" +"%Y-%m-%d") || { usage; exit 1; }
time=$(date -d "${date_in:-"$(date)"}" +"%H:%M") || { usage; exit 1; }
entry="${@:OPTIND}"

entrydirectory="${KAKAPO_HOME:-"$HOME/kakapo"}/journal/${date:0:4}/${date:5:2}"
entryfile="$entrydirectory/$date.md"

if [ -z "$entry" ]
then
  echo $date
  if [ -f "$entryfile" ]
  then
    cat "$entryfile"
  else
    echo "No Entries"
  fi
else
  mkdir -p "$entrydirectory"
  echo "- $time: $entry" >> "$entryfile"
  echo "Added \"$entry\" to $date"
fi