import styles from "./HeaderButton.module.css";

interface IHeaderButtonProps {
  text: string;
}

export function HeaderButton({ text }: IHeaderButtonProps) {
  return <button className={styles.HeaderButton}>{text}</button>;
}
