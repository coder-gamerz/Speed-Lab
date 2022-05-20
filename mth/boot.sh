nasm -f bin -o bootload.iso bootload.asm
qemu-system-x86_64 -hda bootload.iso

