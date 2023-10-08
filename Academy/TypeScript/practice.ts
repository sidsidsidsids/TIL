abstract class User {
    constructor(
        private firstName:string,
        private lastName:string,
        public nickname:string
    ){}
    abstract getNickName():void

    getFullname(){
        return `${this.firstName} ${this.lastName}`
    }

}

class Player extends User{
    getNickName(): void {
        console.log(this.nickname)
    }
}

const nico = new Player('f','l','n')

nico.getFullname

type Food = string;

const kimchi: Food = "delicious"

type WNickname = string
type Friends = Array<string>

type Team = "red" | "blue" | "yellow"
type Health = 1 | 5 | 10

interface Fallguy {
    nickname: string,
    team: Team,
    health: Health
}

const nio :Fallguy = {
    nickname: "nio",
    team: "blue",
    health: 5
}

interface SubFallguy extends Fallguy {
    Event: boolean,
}

const ino : SubFallguy = {
    nickname: "nio",
    team: "blue",
    health: 5,
    Event: true,
}

interface SiteUser {
    firstName: string,
    lastName: string,
    fullName():string
    sayHi(name:string):string
}

interface Human {
    health: number
}

class NormalUser implements SiteUser, Human{
    constructor(
        public firstName:string,
        public lastName:string,
        public health:number
     ) {}
    fullName(): string {
        return `${this.firstName} ${this.lastName}`
    }
    sayHi(name:string){
        return `Hello ${name}. My name is ${this.fullName()}`
    }
}

interface SStorage<T> {
    [key:string]: T
}

class LocalStorage<T> {
    private storage: SStorage<T> = {}
    set(key:string, value:T){
        this.storage[key] = value
    }
    remove(key:string){
        delete this.storage[key]
    }
    get(key:string):T{
        return this.storage[key]
    }
    clear(){
        this.storage = {}
    }
}

const stringsStorage = new LocalStorage<string>()

stringsStorage.get("key")

const booleansStorage = new LocalStorage<boolean>();

booleansStorage.get("xxx")