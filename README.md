# LeafEditor

This tiny script allows you to edit Leaf's level in Black Souls to any integer in range [0, 973078527] without corrupting your save file.

## How to use?

In Windows Explorer, drag your save file (`%blacksouls%\SaveXX.rvdata2`) directly onto the script file. After the script starts, you will see a console with the current Leaf's level. (If the level does not match the actual level **or** the script closes after starting, please report this to the [Issues](https://github.com/R1senDev/LeafEditor/issues) section.)

After that, you will be prompted to enter the desired character level. There are two key points to consider:

1. Too big value will lead in an `OverflowError`. The game dedicates only **4 bytes** to this value.
2. For some reason, the 4-byte Ruby Marshal values become signed. If the new value does not overflow, but is still large, the character level will be negative; this is a bad thing and you don't want it to happen. In such a case, the save file will load normally and the game will still be playable, but if you try to summon Leaf, the game immediately crashes.

After entering the character's level, a file with the same name as the original one will be created, but with the extension `.rvdata2.modified`. Rename it. To avoid the risk of losing your save, use another slot. For example, if the original file name is `Save02.rvdata2`, rename the generated `Save02.rvdata2.modified` file to `Save03.rvdata2`.

**Done!**