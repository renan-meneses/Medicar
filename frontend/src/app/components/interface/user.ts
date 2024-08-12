import { UUID } from "crypto";

export interface User {
    _id?: UUID;
    first_name: string;
    last_name: string;
    email: string;
    password: string;
}
