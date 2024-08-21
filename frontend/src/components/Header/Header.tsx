import { HeaderButton } from "../Buttons/HeaderButton";

import styles from "./Header.module.css";

export function Header() {
  return (
    <header className={styles.header}>
      <div className={styles.stack}>
        <HeaderButton text={"test"} />
        <HeaderButton text={"test2"} />
      </div>
    </header>
  );
}
